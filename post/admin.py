from django.contrib import admin

from .models import Post

class TextInline(admin.StackedInline):
    model = Post

class PostAdmin(admin.ModelAdmin):
    inline = TextInline
    search_fields = ['text',]
    list_filter = ['created_at',]
    list_display = ['created_at']

# Register your models here.
admin.site.register(Post, PostAdmin)