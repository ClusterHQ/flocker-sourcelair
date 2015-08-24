from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/auth/', include('djoser.urls.authtoken')),
    url(r'^api/', include('terminals.api')),
]
