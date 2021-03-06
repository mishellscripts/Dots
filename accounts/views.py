from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

from . import forms
from post.models import Post


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("post:user_view")
    #template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class PostsByUserView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/view.html'

    login_url = reverse_lazy("login")
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
