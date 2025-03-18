import os
from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    """Database URI and unique ressources.

    Attributes:
        uri: database location
        engine: database connection used for session generation
    """

    def __init__(self, uri, auto_migrate=False):
        """Defines all necessary ressources (URI & engine) and create database if necessary."""
        self.uri = uri
        self.engine = create_engine(self.uri, echo=False)
        self.session_factory = sessionmaker(self.engine)

        # Upgrade application to heads
        if auto_migrate:
            dir_uri = os.path.dirname(__file__)
            alembic = Path(dir_uri) / ".." / ".." / "alembic.ini"
            migrations = Path(dir_uri) / ".." / "alembic"
            alembic_cfg = Config(alembic)
            alembic_cfg.set_main_option('script_location', str(migrations))
            alembic_cfg.set_main_option('sqlalchemy.url', self.uri)
            command.upgrade(alembic_cfg, 'head')
