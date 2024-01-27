from django.conf import settings
from django.http import JsonResponse


class APITokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('Authorization')
        expected_api_key = f"Bearer {settings.API_TOKEN}"

        if not api_key or api_key != expected_api_key:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        response = self.get_response(request)

        return response
