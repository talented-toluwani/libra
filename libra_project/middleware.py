import logging
import time
from typing import Any

logger = logging.getLogger(__name__)


class SimpleMiddleWare:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request) -> Any:
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        duration = time.time() - start_time

        logger.info(
            f"{request.method} {request.path} "
            f"completed in {duration:.4f}s"
        )

        return response
    