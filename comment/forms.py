from django import forms

from comment.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('date_of_create','published','post')

