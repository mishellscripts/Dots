from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer
from .nlp_helper import *
from functools import reduce

import nltk
import random
import tflearn
import operator


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
    #Extract important keywords here
    #content = request.REQUEST.get('post')
    #if 'text' in request.session:
        #text = request.session['text']
    post = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.all().order_by('-created_at')

    #posts = Post.objects.filter(text__icontains=post.text)
    #print(words.most_common(15))

    #parse post into single list of words
    words = nltk.word_tokenize(post.text)

    #get frequency of all words
    words = nltk.FreqDist(words)

    # get important keywords of post (also need to check for adverbs that could be same)
    keywords = list(words.keys())[:3]

    #posts must have some of keywords & share same sentiment emotion
    posts = Post.objects.filter(
        reduce(operator.or_, (Q(text__icontains=k) for k in keywords))
    )

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