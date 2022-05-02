
from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include


router = routers.SimpleRouter()
router.register(r'User', views.LoginViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', include(router.urls))
]
