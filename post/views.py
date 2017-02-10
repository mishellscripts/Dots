from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy

from . import forms
from .models import Post

"""def view(request):
    def get_queryset(self):
        return models.Post.objects.all()
    return render(request, 'post/view.html')"""

class PostsView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/view.html'

def post_create(request):
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated():
                post.user = request.user
            post.save()
            # messages.add_message(request, messages.SUCCESS, "Post added!")
            #messages.success(request, ("Post added!"))
            form = forms.PostForm()
    return render(request, './home.html', {'form': form})
