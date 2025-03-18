import logging

import uvicorn

from jardinier.backend import make_app
from jardinier.settings import Settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s")

# Entrypoint
if __name__ == '__main__':
    settings = Settings()
    uvicorn.run(make_app(settings), host="0.0.0.0", port=5000)
