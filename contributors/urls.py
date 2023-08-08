from django.urls import path
from .api import *

urlpatterns = [
    # Contriutors
    path('contributors/', ListContributors.as_view(), name='list_contributors'),
    path('create_contributors/', CreateContributors.as_view(), name='create_contributors'),
    path('contributors/<int:pk>/', GetContributors.as_view(), name='get-contributors'),
    path('contributors/<int:pk>/delete/', DeleteContributors.as_view(), name='contributors_delete'),


    # Contriutors History
    path('contributors_history/', ListContributionHistory.as_view(), name='list_contributors_history'),
    path('create_contributors_history/', CreateContributionHistory.as_view(), name='create_contributors_history'),
    path('contributors_history/<int:pk>/', GetContributionHistory.as_view(), name='get-contributors_history'),

]