# IMPORTS DJANGO
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'blog/',
        include('blog.urls')
    ),
    path(
        'auth/',
        include('authentication.urls')
    ),
    path(
        'volunteers/',
        include('volunteers.urls')
    ),
    path(
        'contributors/',
        include('contributors.urls')
    ),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
