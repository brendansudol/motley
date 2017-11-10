from django.conf.urls import url
from rest_framework.authtoken import views

from api.views import LocationListView, UserListView


urlpatterns = [
    url(r'^token-auth', views.obtain_auth_token),

    url(r'^locations/$', LocationListView.as_view()),
    url(r'^users/$', UserListView.as_view()),
]
