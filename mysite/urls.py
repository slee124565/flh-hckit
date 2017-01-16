"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
#from django.contrib import admin

from fibaro.api import ApiSceneView, ApiGoodbyeView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    
    url(r'^api/s/v1/(?P<name>[A-Za-z\ ]+)', ApiSceneView.as_view(), name='api_scene'),
    url(r'^api/s/v1_1', ApiGoodbyeView.as_view(), name='api_goodbye_scene'),
    
]
