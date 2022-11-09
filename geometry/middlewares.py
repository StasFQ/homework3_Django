import datetime

from .models import Logs


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin/'):
            Logs.objects.create(path=request.path, method=Logs.Method[request.method])

        response = self.get_response(request)

        return response
