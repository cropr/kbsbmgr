# copyright Ruben Decrop 2012 - 2021
# parts are copyrighted Chessdevil Consulting

from reddevilmgr.main import app
from reddevil.core import get_settings
import ansible_runner
from reddevilmgr.models.mgrrequest import MgrRequest
from reddevilmgr.api import domain_mapping


@app.post("/python/checkout")
def api_checkout(p: MgrRequest):
    settings = get_settings()
    domain = p.email.split("@")[-1]
    user = p.user.lower()
    project = domain_mapping.get(domain)
    r = ansible_runner.run(
        private_data_dir=settings.ANSIBLE_PATH.as_posix(),
        playbook="checkout.yml",
        extravars={"project": project, "user": user, "repo_branch": p.branch},
    )
    print("r", vars(r))
    return {"status": r.status}
