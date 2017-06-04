from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from accounts import views as views2


urlpatterns = [
    url(r'^view/related', views.post_search, name='view_related'),
    #url(r'^view/(?P<keyword>\w+)/', views.PostsSearchView.as_view(), name='view_related'),
    url(r'^view/', views.PostsView.as_view(), name='view'),
]

