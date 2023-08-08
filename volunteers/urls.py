from django.urls import path
from .api import *

urlpatterns = [
    path('volunteers/', ListVolunteers.as_view(), name='list_volunteers'),
    path('create_volunteers/', CreateVolunteers.as_view(), name='create_volunteers'),
    path('volunteers/<int:pk>/', GetVolunteers.as_view(), name='get-volunteers'),
    path('volunteers/<int:pk>/delete/', DeleteVolunteers.as_view(), name='volunteers_delete'),
]
