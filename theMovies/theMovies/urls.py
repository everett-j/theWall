from django.conf.urls import url, include	# added an import!
# from django.contrib import admin              # comment out, or just deletecopy
urlpatterns = [
    url(r'^wall/', include('apps.app_wall.urls', namespace='wall')),
    url(r'^trips/', include('apps.belt.urls', namespace='belt')),
    url(r'^new/', include('apps.app_two.urls', namespace='new')),
     url(r'^exam2/', include('apps.app_exam2.urls', namespace='exam2')),
    url(r'^movies/', include('apps.movies.urls', namespace='movies')),
    url(r'^', include('apps.app_login.urls', namespace='login')),

    	# use your app_name here

]