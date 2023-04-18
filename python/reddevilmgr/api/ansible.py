# copyright Ruben Decrop 2012 - 2021
# parts are copyrighted Chessdevil Consulting

import logging
from reddevilmgr.main import app
from reddevil.core import get_settings
import ansible_runner

logger = logging.getLogger("reddevilmgr")


@app.post("/python/ansible")
def api_ansible():
    settings = get_settings()
    logger.info(f"ANSIBLE_PATH: {settings.ANSIBLE_PATH.as_posix()}")
    r = ansible_runner.run(
        private_data_dir=settings.ANSIBLE_PATH.as_posix(), playbook="hello.yml"
    )
    print("r", vars(r))
    return {"status": r.status}
