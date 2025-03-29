import configparser
from pathlib import Path


class Settings:
    """Parameters of the application read from settings.ini
    
    Attributes:
        debug: Flag to set debug options in all application
        jwt_secret_key: secret to generate JWTs
        database_uri: URI to connect to the database
    """
    debug: bool = True
    jwt_secret_key: str = "sssssssss"
    database_uri: str = "sqlite+pysqlite:///sqlite.db"

    def __init__(self):
        """Lis le fichier de configuration depuis le fichier settings.ini"""
        cfg = configparser.ConfigParser()
        cfg.read(Path(__file__).parent / ".." / "settings.ini")

        self.debug = cfg['DEFAULT'].getboolean('debug', fallback=self.debug)
        self.jwt_secret_key = cfg['DEFAULT'].get('jwt_secret_key', fallback=self.jwt_secret_key)
        self.database_uri = cfg['DEFAULT'].get('database_uri', fallback=self.database_uri)
