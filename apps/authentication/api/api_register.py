from ninja import Router
from django.http import HttpResponse, JsonResponse

authentication_router = Router()

@authentication_router.get('register/')
def register(request: HttpResponse):
    return JsonResponse({'status': 'success'})