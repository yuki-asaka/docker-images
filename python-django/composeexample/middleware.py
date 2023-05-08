import logging
import time

from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger(__name__)

class CustomErrorHandlerMiddleware(MiddlewareMixin):
    """
    # This middleware is used to handle exceptions raised by the view functions.
    # https://docs.djangoproject.com/en/4.2/topics/http/middleware/#process-exception
    """
    def process_exception(self, request, exception):
        logger.exception(exception)
        raise exception


class TimeMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - request.start_time
        response["X-Page-Duration-ms"] = int(duration * 1000)
        logger.info(f"\"{request.method} {request.get_full_path()}\" {response.status_code} {duration:.2f}s")
        return response
