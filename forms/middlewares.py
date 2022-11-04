import json

from .models import Logs


class LogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin/'):
            post_data = json.dumps(request.POST)
            get_data = json.dumps(request.GET)
            log = Logs(path=request.path, method=Logs.RequestMethods[request.method],
                       get_data=get_data, post_data=post_data)
            log.save()

        response = self.get_response(request)

        # Code that is executed in each request after the view is called
        return response
