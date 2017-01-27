"""smapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views
from post import views as view2

urlpatterns = [
    url(r'^$', view2.post_create, name='main'),
    #url(r'^$', views.main_page, name='main'),
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^admin/', admin.site.urls),
    url(r'^about/', views.about, name='about'),
    url(r'^signin/', views.sign_in, name='sign_in'),
    url(r'^suggestions/$', views.suggestion_view, name='suggestion'),
]
