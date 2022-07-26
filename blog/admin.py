from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title_post', 'post_info', 'slug', 'date']
    search_fields = ['title_post']
    exclude = ['slug']

