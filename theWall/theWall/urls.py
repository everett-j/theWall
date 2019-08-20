from django.conf.urls import url, include	# added an import!
# from django.contrib import admin              # comment out, or just deletecopy
urlpatterns = [
    url(r'^', include('apps.app_wall.urls')),
    url(r'^', include('apps.app_login.urls')),	# use your app_name here

]