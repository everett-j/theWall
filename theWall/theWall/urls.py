from django.conf.urls import url, include	# added an import!
# from django.contrib import admin              # comment out, or just deletecopy
urlpatterns = [
    url(r'^wall/', include('apps.app_wall.urls', namespace='wall')),
    url(r'^', include('apps.app_login.urls', namespace='login')),

    	# use your app_name here

]