from django.contrib import admin
from .models import Author, Post, Comment, Rating

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__user__username')
    list_filter = ('author', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('post__title', 'author__username')
    list_filter = ('created_at',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'score')
    search_fields = ('post__title', 'author__username')
    list_filter = ('score',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)
