# coding=utf8

from .models import CommentChild, CommentParent
from django.forms import ModelForm


class CommentParentForm(ModelForm):
    class Meta:
        model = CommentParent
        fields = ('commentParent_text',)

class CommentChildForm(ModelForm):
    class Meta:
        model = CommentChild
        fields = ('commentChild_text',)