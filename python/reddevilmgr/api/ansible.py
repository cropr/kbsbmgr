# copyright Ruben Decrop 2012 - 2021
# parts are copyrighted Chessdevil Consulting

from reddevilmgr.main import app
from reddevil.core import get_settings
import ansible_runner


@app.post("/python/ansible")
def api_root():
    settings = get_settings()
    r = ansible_runner.run(
        private_data_dir=settings.ANSIBLE_PATH.as_posix(), playbook="hello.yml"
    )
    print("r", vars(r))
    return {"status": r.status}
