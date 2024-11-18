
from format_logger.logger import logger

class base_pipeline:

    _pipeline_name = "base_pipeline"

    def __init__(self, log : logger) -> None:
        log = log.start_function(f"{self._pipeline_name}.__ini__")

        self._name = "base_pipeline"

        log.end_function()

    def execute(self, log : logger) -> None: 
        log = log.start_function(f"{self._pipeline_name}.execute")

        log.INFO("Test message inside pipeline")

        log.end_function()

    def get_response(self, log : logger) -> dict:
        log = log.start_function(f"{self._pipeline_name}.get_response")

        response = {
            "message" : "hello world!",
            "pipeline" : self._pipeline_name
        }

        log.end_function()
        return response
        

