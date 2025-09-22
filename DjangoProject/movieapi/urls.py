from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
