from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_create', )
    search_fields = ('author', 'text')
    list_filter = ('date_of_create', 'published')
    list_display = ('author', 'published', 'date_of_create')
    list_editable = ('published', ) # изменять в списке постов опубликовано