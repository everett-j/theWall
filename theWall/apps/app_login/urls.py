from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^login$', views.loginregister),
    url(r'^register$', views.register),
    url(r'^logme$', views.login),
    url(r'^logout$', views.logout),
    url(r'^success$', views.success),
]