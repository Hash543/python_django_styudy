from django.contrib import admin
from .models import Post

@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
    ordering = ['-created_at']
    list_per_page = 20
    fieldsets = [
      ('文章資訊', {'fields': ['title', 'content']})
    ]