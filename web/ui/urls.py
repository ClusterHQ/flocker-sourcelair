from django.conf.urls import url

from ui import views

urlpatterns = [
    url(r'^$', views.register_view, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^terminal/$', views.terminal_view, name='terminal'),
]