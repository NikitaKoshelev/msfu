from django.forms import ModelForm

from .models import Likes


class AddLike(ModelForm):
    class Meta:
        model = Likes
