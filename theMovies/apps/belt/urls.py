from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.redirect_home),
    url(r'^dashboard$', views.belt),
    url(r'^(?P<t_id>\d+)$', views.detail_trip),
    url(r'^new$', views.add_trip),
    url(r'^new_trip$', views.new_trip),
    url(r'^update$', views.update_redirect),
    url(r'^edit_trip$', views.cancel_redirect),
    url(r'^edit/(?P<t_id>\d+)$', views.edit_trip),
    url(r'^delete/(?P<trips_id>\d+)$', views.trips_delete),


]