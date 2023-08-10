from django.urls import path
from .api import *
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('t', views.t, name="t"),
    path('login/user/', LoginUser.as_view(), name="login_user"),
    path('users/', ListUsers.as_view(), name='user_list'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('users/<int:pk>/get/', UserDetails.as_view(), name='get_user'),
    path('users/<int:pk>/update/', UserUpdate.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='user_delete'),
    path('token/refresh/user/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activate_account/<uid4>/<token>/', ActivateAccountView.as_view(), name='activate_account'),
]
