from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ( 'texto','fecha_creacion')
    search_fields = ['texto',]

admin.site.register(Post, PostAdmin)