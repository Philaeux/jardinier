from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import datetime, UTC
from typing import Annotated

import adafruit_ahtx0
import board
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Depends
from fastapi.requests import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter, BaseContext

from jardinier.database.measure import Measure
from jardinier.graphql.schema import schema
from jardinier.settings import Settings
from jardinier.utils.helpers import check_migration


@dataclass
class AppContext(BaseContext):
    settings: Settings
    session: Session

def make_app(settings: Settings):
    # Database
    engine = create_engine(settings.database_uri)
    check_migration(settings.database_uri)

    # Periodic tasks scheduler
    scheduler = AsyncIOScheduler(timezone=UTC)

    # Session dependency
    def get_session():
        with Session(engine, expire_on_commit=False) as session:
            yield session
    SessionDep = Annotated[Session, Depends(get_session)]

    # App creation
    @asynccontextmanager
    async def lifespan(fast_app: FastAPI):
        scheduler.start()
        yield
        scheduler.shutdown()

    app = FastAPI(lifespan=lifespan)
    app.engine = engine
    app.settings = settings
    i2c = board.I2C()
    sensor = adafruit_ahtx0.AHTx0(i2c)

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://jard.the-cluster.org",
            "http://192.168.0.35",
            "http://localhost:4200"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # GraphQL
    async def get_context(session: SessionDep):
        """Context passed to all GraphQL functions. Give database access"""
        return AppContext(settings=settings, session=session)

    graphql_app = GraphQLRouter(
        schema,
        graphql_ide="graphiql" if settings.debug else None,
        context_getter=get_context,
    )
    app.include_router(graphql_app, prefix="/api/graphql")

    # Static files
    # app.mount("/aaa, StaticFiles(directory=any path), name="data")

    # Classic REST endpoints
    @app.get('/api/hello')
    async def hello(request: Request):
        return {"message": "Hello World"}

    @scheduler.scheduled_job('interval', seconds=10*60)
    async def save_data():
        with Session(engine) as session:
            measure = Measure(time=datetime.now(UTC), temperature=sensor.temperature, humidity=sensor.relative_humidity)
            session.add(measure)
            session.commit()

    return app
