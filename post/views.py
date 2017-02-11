from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer

class PostsView(ListView):
    model = Post
    serializer_class = PostSerializer
    context_object_name = 'posts'
    template_name = 'post/public_view.html'

"""class PostsSearchView(ListView):
    model = Post
    template_name = 'post/view.html'
    selected_related = ['text']
    context_object_name = 'related_posts'

    def get_queryset(self):
        # Extract important keywords here
        content = self.request.REQUEST.get('q')
        #content = self.request.session['content']
        posts = Post.objects.filter(text__icontains=content)
        return posts
        #return Post.objects.filter(text__icontains=query)
"""

def post_search(request, post_id):
    # Extract important keywords here
    #content = request.REQUEST.get('post')
    #if 'text' in request.session:
        #text = request.session['text']
    post = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.filter(text__icontains=post.text)

    return render(request, 'post/public_view.html', {'posts': posts})

def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated():
                post.user = request.user
            #post_text = request.POST['text']

            post.save()
            # messages.add_message(request, messages.SUCCESS, "Post added!")
            #messages.success(request, ("Post added!"))
            #form = PostForm()
            #return HttpResponseRedirect('/view/related')
            #return HttpResponseRedirect(reverse_lazy('view_related'), {'post': post})
            return redirect('view_related', post_id=post.id)
    return render(request, './home.html', {'form': form})

"""class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home.html'

    return redirect('/view/%s' %)"""