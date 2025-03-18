import pytest
from starlette.testclient import TestClient

from templates.backend import make_app
from templates.database.a import A
from templates.settings import Settings


@pytest.fixture(scope="session")
def build_app():
    """On crée une mock app pour toute la session de test."""
    settings = Settings()
    settings.debug = True

    yield TestClient(make_app(settings))


@pytest.fixture()
def mock_app(build_app):
    """Empty tables before every test..."""
    with build_app.app.database.session_factory() as session:
        # session.query(A).delete()
        session.commit()

    # Make app
    yield build_app
