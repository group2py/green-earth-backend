from django.urls import path
from .api import *

urlpatterns = [
    path('users/', ListUsers.as_view(), name='user_list'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('users/<int:pk>/get/', UserDetails.as_view(), name='get_user'),
    path('users/<int:pk>/update/', UserUpdate.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='user_delete'),
    path('activate_account/<uid4>/<token>/', ActivateAccountView.as_view(), name='activate_account'),
]
