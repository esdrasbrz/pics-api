from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'albuns', views.AlbumViewSet)
router.register(r'fotos', views.FotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
