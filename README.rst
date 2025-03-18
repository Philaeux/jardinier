Fullstack Website Template - Angular Frontend, Python FastAPI Backend
=======================================================================

To use this template, rename all mentions of "templates" in the filenames and file content with the codename of your project.

Backend
--------

HTTP Web Backend using the following technologies:

* Python 3.11+
* `Poetry <https://python-poetry.org/>`_ to manage Python Virtual Environment and dependencies.
* `Docker <https://www.docker.com/>`_ to manage deployment in production and database in development.
* `Postgresql <https://www.postgresql.org/>`_ as database choice.
* `SQLAlchemy <https://www.sqlalchemy.org/>`_ as ORM (Object Relational Mapper) library.
* `Alembic <https://alembic.sqlalchemy.org/en/latest/>`_ to manage database migrations.
* `Strawberry <https://strawberry.rocks/>`_ as GraphQL API Framework.
* `FastAPI <https://fastapi.tiangolo.com/>`_ as Asynchronous Web Framework.
* `Uvicorn <https://www.uvicorn.org/>`_ as Asynchronous Web Server.
* `Pytest <https://docs.pytest.org/en/8.0.x/>`_ as Test Framework.
* `Sphinx <https://www.sphinx-doc.org/en/master/>`_ to generate documentation from codebase.

Frontend
---------

Single Page App frontend using the following technologies:

* `Angular <https://angular.dev/>`_ 19
* `Angular Material <https://material.angular.io/>`_

Setup
-------

You first need to create 2 configuration files:

- Create `./docker/docker.env` file with as structure similar to `./docker/docker.example.env`
- Create `./templates-backend/src/settings.ini` file with a structure similar to `./templates-backend/src/settings.example.ini`

Production
------------

If everything is properly setup (configuration files), its only a git pull and restart::

    cd docker
    git pull
    docker compose --env-file docker.env build
    docker compose --env-file docker.env up --build -d

Development
------------

If you wish to use a postgresql database similar to production in dev, use the .dev compose file::

    # Starts a PostgreSQL similar to prod
    cd docker
    docker compose -f docker-compose.dev.yaml --env-file docker.env up
    # Optional, make a backup of production database and use it as a snapshot for dev purposes
    # On server:
    sudo rsync -av --no-perms --delete --chown=$(whoami) ../templates_postgres_data/ ~/templates_postgres_save
    sudo chown -R $(whoami):$(whoami) ../templates_postgres_save
    # On machine:
    sudo rsync -avz --stats --delete $(whoami)@<server>:~/templates_postgres_save/ ../templates_postgres_data
    # On server:
    sudo rm -rf ~/templates_postgres_save

To run the backend, using poetry::

    # Make sure you have poetry
    python -m pip install pipx
    python -m pipx install poetry
    # Install dependencies
    cd templates-backend
    poetry install --with docs,tests
    # Run tests
    cd src
    poetry run pytest
    # Get information about the virtual environment (to setup in your ide)
    poetry env info
    # Run
    cd src
    poetry run python main.py
    # Generate documentation
    cd docs
    poetry run sphinx-build . _build
    # If you want to remove your venv associated
    poetry env remove python

To generate a new database migration, use alembic::

    poetry run alembic revision --autogenerate

Before using the frontend, make sure you have `nvm` installed. To run the frontend, using node::

    # Check that nvm is ready to be used:
    nvm version
    # Install a running version of node:
    nvm install lts
    # Set the installed version as the one to use:
    nvm use lts
    # Check that node is ready to be used
    node --version
    npm --version
    # Install angular global library:
    npm install -g @angular/cli
    # Install frontend libraries
    cd templates-frontend
    npm install
    # Start the project:
    ng serve
