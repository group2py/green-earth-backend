from django.urls import path
from .api import *

urlpatterns = [
    # New voluntary
    path('list/', ListVolunteers.as_view(), name='list_volunteers'),
    path('create/', CreateVolunteers.as_view(), name='create_volunteers'),
    path('<int:pk>/get/', GetVolunteers.as_view(), name='get-volunteers'),
    path('<int:pk>/delete/', DeleteVolunteers.as_view(), name='volunteers_delete'),
    path('user/<int:pk>/', VerifyVoluntary.as_view(), name="user_volunteer"),

    # New Mission
    path('mission/list/', ListNewMission.as_view(), name='list_mission'),
    path('mission/create/', CreateNewMission.as_view(), name='create_mission'),
    path('mission/<int:pk>/get/', GetNewMission.as_view(), name='get_mission'),
]
