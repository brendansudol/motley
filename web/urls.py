from django.conf.urls import url

from web.views.home import HomeView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
]
