from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^view/', views.view, name='view'),
    url(r'^view/my/', views.UserView.as_view(template_name = 'post/user_view.html'), name="user_view"),
]

