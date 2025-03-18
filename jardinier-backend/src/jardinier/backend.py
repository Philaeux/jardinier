from contextlib import asynccontextmanager

import adafruit_ahtx0
import board
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyLoader

from jardinier.database.database import Database
from jardinier.graphql.schema import schema
from jardinier.settings import Settings
from jardinier.utils.repeat_every import repeat_every


def make_app(settings: Settings):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await save_data()
        yield
        # Add shutdown functions here

    app = FastAPI(lifespan=lifespan)
    i2c = board.I2C()
    sensor = adafruit_ahtx0.AHTx0(i2c)

    # Database
    database = Database(uri=settings.database_uri, auto_migrate=True)
    app.database = database
    app.settings = settings

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            settings.frontend_uri,
            "http://localhost:4200"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # GraphQL
    async def get_context():
        """Context passed to all GraphQL functions. Give database access"""
        return {
            "settings": settings,
            "session": Session(database.engine),
            "sqlalchemy_loader": StrawberrySQLAlchemyLoader(bind=database.session_factory()),
        }


    graphql_app = GraphQLRouter(
        schema,
        graphql_ide="graphiql" if settings.debug else None,
        context_getter=get_context,
    )
    app.include_router(graphql_app, prefix="/graphql")

    # Static files
    # app.mount("/aaa, StaticFiles(directory=any path), name="data")

    # Classic REST endpoints
    @app.get('/hello')
    async def hello(request: Request):
        return {"message": "Hello World"}

    @repeat_every(seconds=60)
    async def save_data():
        print("Temperature: %0.1f C" % sensor.temperature)
        print("Humidity: %0.1f %%" % sensor.relative_humidity)

    return app
