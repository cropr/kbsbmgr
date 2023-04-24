# copyright Ruben Decrop 2012 - 2021
# parts are copyrighted Chessdevil Consulting

from reddevilmgr.main import app


@app.get("/python")
def api_root():
    return {"hello": "world"}


# maps a domain to a projectname
domain_mapping = {"kosk.be": "kosk", "bycco.be": "bycco", "frbe-kbsb-ksb.be": "kbsb"}

import reddevilmgr.api.ansible
import reddevilmgr.api.checkin
import reddevilmgr.api.checkout
