from django.urls import path
from .api import *

urlpatterns = [
    # Denunciations
    path('denunciations/', ListCrimeDenunciations.as_view(), name='list_denunciationss'),
    path('create_denunciations/', CreateCrimeDenunciations.as_view(), name='create_denunciations'),
    path('denunciations/<int:pk>/get/', GetCrimeDenunciations.as_view(), name='get_denunciations'),

    # Blog Post
    path('post/', ListBlogPost.as_view(), name='list_post'),
    path('create_post/', CreateBlogPost.as_view(), name='create_post'),
    path('post/<int:pk>/', GetBlogPost.as_view(), name='get_post'),
    path('post/<int:pk>/delete/', DeleteBlogPost.as_view(), name='post_delete'),
    path('post_update/<int:pk>/update/', UpdateBlogPost.as_view(), name='update_post'),
    
    # Media Ong
    path('media/', ListMediaOng.as_view(), name='list_media'),
    path('create_media/', CreateMediaOng.as_view(), name='create_media'),
    path('media/<int:pk>/get/', GetMediaOng.as_view(), name='get_media'),
    path('media/<int:pk>/update/', GetMediaOng.as_view(), name='update_media'),
    
    # New Mission
    path('mession/', ListCrimeDenunciations.as_view(), name='list_mession'),
    path('create_mession/', CreateCrimeDenunciations.as_view(), name='create_mession'),
    path('mession/<int:pk>/get/', GetCrimeDenunciations.as_view(), name='get_denunciations'),
    path('mession/<int:pk>/delete/', DeleteNewMission.as_view(), name='mession_delete'),
]