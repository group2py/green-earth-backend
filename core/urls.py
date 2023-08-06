# IMPORTS API APPS
from blog import api as api_blog
from volunteers import api as api_volunteers
from contributors import api as api_contributors
from authentication import api as api_authentication

# IMPORT DJANGO REST FRAMEWORK
from rest_framework import routers

# IMPORTS DJANGO
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Registared routers
router = routers.DefaultRouter()
router.register(r'blog', api_blog.CreateBlogPost)
router.register(r'media', api_blog.CreateMediaOng)
router.register(r'users', api_authentication.RegisterUser)
router.register(r'crime', api_blog.CreateCrimeDenunciations)
router.register(r'list_volunteers', api_volunteers.CreateVolunteers)
router.register(r'list_contributors', api_contributors.CreateContributors)
router.register(r'list_contributors_history', api_contributors.CreateContributionHistory)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Routers api
    path('', include(router.urls)),
    path('get_blog/', api_blog.CreateBlogPost.as_view(actions={'get': 'list'})),
    path('get_media/', api_blog.CreateMediaOng.as_view(actions={'get': 'list'})),
    path('get_users/', api_authentication.RegisterUser.as_view(actions={'get': 'list'})),
    path('get_crime/', api_blog.CreateCrimeDenunciations.as_view(actions={'get': 'list'})),
    path('get_volunteers/', api_volunteers.CreateVolunteers.as_view(actions={'get': 'list'})),
    path('get_contributors/', api_contributors.CreateContributors.as_view(actions={'get': 'list'})),
    path('get_contributors_history/', api_contributors.CreateContributionHistory.as_view(actions={'get': 'list'})),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
