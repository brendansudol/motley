from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('web.urls', namespace='web')),
    url(r'^api/', include('api.urls', namespace='api')),
]
