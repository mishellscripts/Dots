from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from accounts import views as views2


urlpatterns = [
    url(r'^view/', views.PostsView.as_view(), name='view'),
]

