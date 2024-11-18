
from flask import Flask
from format_logger.logger import logger

from settings.globals import api_name

app = Flask(__name__)

# ------------- Endpoints -------------

# ------ Base Enpoint ------

@app.route("/endpoint")
def endpoint() -> dict:
    log = logger(api_name, "endpoint")

    from pipelines.base import base_pipeline

    p = base_pipeline(log)
    p.execute(log)
    response = p.get_response(log)

    log.end_function()
    return response


# ------------- Run API -------------

app.run(host = "0.0.0.0", port = "8080", threaded = True)
