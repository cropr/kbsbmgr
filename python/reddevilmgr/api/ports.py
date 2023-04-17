# copyright Ruben Decrop 2012 - 2021
# parts are copyrighted Chessdevil Consulting

from reddevilmgr.main import app
from reddevil.core import get_settings
from reddevilmgr.models.user import Person
from fastapi.responses import Response
from typing import Dict
import yaml
from pathlib import Path
from reddevilmgr.api import domain_mapping


@app.post(
    "/python/ports",
)
def api_ports(p: Person):
    domain = p.email.split("@")[-1]
    user = p.user.lower()
    project = domain_mapping.get(domain)
    if not project:
        return Response(content="Project not found", status_code=404)
    configpath = Path(".") / "ansible" / "vars" / f"{project}.yml"
    try:
        with open(configpath, "r") as fy:
            try:
                config = yaml.safe_load(fy)
            except yaml.YAMLError:
                config = None
        if not config:
            return Response(status_code=400)
        users = config.get("users")
        reply = users.get(user)
    except FileNotFoundError as e:
        print(f"could not open {configpath}")
        return Response(status_code=404)
    print("config", config)
    return config.get("users", {}).get(user, {})
