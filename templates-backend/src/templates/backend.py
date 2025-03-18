from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request

from strawberry.fastapi import GraphQLRouter
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyLoader

from templates.settings import Settings
from templates.database.database import Database
from templates.graphql.schema import schema


def make_app(settings: Settings):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Add startup functions here
        yield
        # Add shutdown functions here

    app = FastAPI(lifespan=lifespan)

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
        """Contexte passed to all GraphQL functions. Give database access"""
        return {
            "settings": settings,
            "session_factory": database.session_factory,
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

    return app
