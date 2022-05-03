
from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include


router = routers.SimpleRouter(trailing_slash=False)
router.register('user', views.LoginViewSet)

urlpatterns = [
    # path('', views.home, name="home"),
    path('login/', include(router.urls))
]
