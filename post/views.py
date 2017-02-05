from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import models, forms

class UserView(LoginRequiredMixin, generic.ListView):
    model = models.Post
    template_name = 'post/user_view.html'

def view(request):
    return render(request, 'post/view.html')

def post_create(request):
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # messages.add_message(request, messages.SUCCESS, "Post added!")
            #messages.success(request, ("Post added!"))
            form = forms.PostForm()
    return render(request, './home.html', {'form': form})
