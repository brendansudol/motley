from django.conf.urls import include, url

from rest_framework import routers
from rest_framework.authtoken import views

from api.views import LocationListView, UserCreateView, UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^new-user$', UserCreateView.as_view()),
    url(r'^token-auth', views.obtain_auth_token),

    url(r'^locations/$', LocationListView.as_view()),
]
