from django.urls import path
from .api import *

urlpatterns = [
    path('list/', ListVolunteers.as_view(), name='list_volunteers'),
    path('create/', CreateVolunteers.as_view(), name='create_volunteers'),
    path('<int:pk>/get/', GetVolunteers.as_view(), name='get-volunteers'),
    path('<int:pk>/delete/', DeleteVolunteers.as_view(), name='volunteers_delete'),
]
