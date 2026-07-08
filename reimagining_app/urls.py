from django.urls import include, path

from . import views
from .api import router

urlpatterns = [
    path('', views.home, name="home"),
    path('api/', include(router.urls)),
]