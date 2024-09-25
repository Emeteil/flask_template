from settings import *

from flask import render_template
from utils.api_response import *

import api.admin
import events

@app.route("/")
async def mainPage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(
        host = settings['host'], 
        port = settings['port'],
        debug = settings['debug']
    )