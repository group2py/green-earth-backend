# Responsible for creating our urls
from ninja import NinjaAPI
from django.http import HttpResponse, JsonResponse

# Create api instance
api = NinjaAPI()


@api.get('test/')
def test(request: HttpResponse):
    return JsonResponse({'Welcome': 'Hello, World!'})