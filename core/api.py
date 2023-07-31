from ninja import NinjaAPI
from apps.home.api.api import home_router
from apps.authentication.api.api_register import authentication_router


api = NinjaAPI()
api.add_router('home/', home_router)
api.add_router('auth/', authentication_router)
