#    Copyright 2022 Chessdevil Consulting

import os, os.path
import yaml
from pathlib import Path

# paths
ANSIBLE_PATH = Path(os.environ.get("ANSIBLE_PATH", "../ansible"))
SECRETS_PATH = Path(os.environ.get("SECRETS_PATH", ""))
COLORLOG = False
LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(asctime)s %(name)s %(message)s",
        },
        "color": {
            "format": "%(log_color)s%(levelname)s%(reset)s: %(asctime)s %(bold)s%(name)s%(reset)s %(message)s",
            "()": "reddevil.core.colorlogfactory.c_factory",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "reddevilmgr": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "reddevil": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "fastapi": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

try:
    from local_settings import *

    ls = "local settings loaded"
except ImportError:
    ls = "No local settings found"

if COLORLOG:
    LOG_CONFIG["handlers"]["console"]["formatter"] = "color"  # type: ignore
