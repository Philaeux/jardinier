import logging

import uvicorn

from templates.backend import make_app
from templates.settings import Settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s")

# Entrypoint
if __name__ == '__main__':
    settings = Settings()
    uvicorn.run(make_app(settings), host="0.0.0.0", port=5000)
