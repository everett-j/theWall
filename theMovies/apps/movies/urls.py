from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.movies),
    url(r'^(?P<movies_id>\d+)$', views.movie_detail),
    url(r'^movies/add$', views.add_movie),
    url(r'^add_review$', views.add_review),
    url(r'^add_movie$', views.add_redirect),
    url(r'^delete_review$', views.delete_review),

]