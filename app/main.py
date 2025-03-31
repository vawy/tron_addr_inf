import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import uvicorn
from fastapi import FastAPI

from app.utils.base import bind_routes, bind_events
from app.handlers import routes
from app.settings import db_settings


def make_app(db_settings) -> FastAPI:
    app = FastAPI(
        title="Tron wallet info",
        description="",
        docs_url="/api/tron_wallet/swagger"
    )

    bind_events(app=app, db_url=db_settings.database_url)
    bind_routes(app=app, routes=routes)
    return app


if __name__ == "__main__":
    uvicorn.run(
        make_app(db_settings=db_settings)
    )
