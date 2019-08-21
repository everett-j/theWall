from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.wall),
    url(r'^wall$', views.wall),
    url(r'^wall_post$', views.wall_post),
    url(r'^comment_post$', views.comment_post),
    url(r'^delete/(?P<comments_id>\d+)$', views.comments_delete),

]