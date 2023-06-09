# copyright Ruben Decrop 2012 - 2021
# parts are copyrighted Chessdevil Consulting

from reddevilmgr.main import app
from reddevil.core import get_settings
from reddevilmgr.models.user import MgrRequest
from reddevilmgr.api import domain_mapping
import ansible_runner

# TODO not working for the moment


@app.post("/python/preview")
def api_preview(p: MgrRequest):
    settings = get_settings()
    domain = p.email.split("@")[-1]
    user = p.user.lower()
    project = domain_mapping.get(domain)
    r = ansible_runner.run(
        private_data_dir=settings.ANSIBLE_PATH.as_posix(),
        playbook="launchpreview.yml",
        extravars={"project": project, "user": user},
    )
    print("r", vars(r))
    return {"status": r.status}
