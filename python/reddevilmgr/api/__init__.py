# copyright Ruben Decrop 2012 - 2021
# parts are copyrighted Chessdevil Consulting

from reddevilmgr.main import app


@app.get("/python")
def api_root():
    return {"hello": "world"}


domain_mapping = {
    "kosk.be": "kosk",
    "bycco.be": "bycco",
    "frbe-kbsb-ksb.be": "kbsb"
}

import reddevilmgr.api.ansible
import reddevilmgr.api.setupwork
import reddevilmgr.api.preview
import reddevilmgr.api.production
import reddevilmgr.api.ports
