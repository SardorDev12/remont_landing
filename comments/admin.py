from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','job', 'comment')
    search_fields = ('name',)

admin.site.register(Comment, CommentAdmin)
