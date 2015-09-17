from django.conf.urls import url

from ui import views

urlpatterns = [
    url(r'^$', views.register_view),
    url(r'^login/$', views.login_view),
]