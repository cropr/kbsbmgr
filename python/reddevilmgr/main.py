# copyright Ruben Decrop 2012 - 2022
# copyright Chessdevil Consulting 2015 - 2022

import os.path
import logging, logging.config

from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from reddevil.core import register_app, get_settings

# load and register app
app = FastAPI(
    title="ReddevilMgr",
    description="reddevil manager",
    version="0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
register_app(app, "reddevilmgr.settings", "/api")

# get settings
settings = get_settings()
logging.config.dictConfig(settings.LOG_CONFIG)
logger = logging.getLogger("reddevilmgr")
logger_g = logging.getLogger("reddevilmgr")
logger.handlers = logger_g.handlers
logger.setLevel(logger_g.level)
logger.info(f"Starting website reddevilmgr ...")

# show local settings loaded or not
from reddevilmgr.settings import ls

logger.info(ls)

# import api endpoints
import reddevilmgr.api

logger.info(f"Api layer loaded")

#    Simplify operation IDs so that generated API clients have simpler function
#    names.
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name[4:]
