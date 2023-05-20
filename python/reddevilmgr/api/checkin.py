# copyright Ruben Decrop 2012 - 2021
# parts are copyrighted Chessdevil Consulting

import logging
from reddevilmgr.main import app
from reddevil.core import get_settings
from reddevilmgr.models.mgrrequest import MgrRequest
from reddevilmgr.api import domain_mapping
import ansible_runner

logger = logging.getLogger("reddevilmgr")


@app.post("/python/checkin")
def api_checkin(p: MgrRequest):
    settings = get_settings()
    logger.info(f"Doing checkin on branch {p.branch}")
    domain = p.email.split("@")[-1]
    user = p.user.lower()
    project = domain_mapping.get(domain)
    r = ansible_runner.run(
        private_data_dir=settings.ANSIBLE_PATH.as_posix(),
        playbook="checkin.yml",
        extravars={
            "project": project,
            "user": user,
            "repo_branch": p.branch,
        },
    )
    print("r", vars(r))
    return {"status": r.status}
