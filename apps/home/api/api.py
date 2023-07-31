from ninja import Router
from django.http import HttpResponse, JsonResponse

home_router = Router()

@home_router.get('')
def home(request: HttpResponse):
    return JsonResponse({'status': 'success'})