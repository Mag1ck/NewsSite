from django.conf import settings
from django.shortcuts import redirect


class HttpsRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.is_secure() and settings.DEBUG == False:
            # Redirect to HTTPS
            secure_url = request.build_absolute_uri().replace('http://', 'https://')
            return redirect(secure_url)

        response = self.get_response(request)
        return response
