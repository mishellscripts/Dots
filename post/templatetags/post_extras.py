from django import template

from post.models import Post


register = template.Library()

def get_keyword():
    return 'hi'