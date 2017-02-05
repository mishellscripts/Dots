from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^view/', views.view, name='view'),
    url(r'^view/my/', views.UserView.as_view(), name="user_view"),
]

