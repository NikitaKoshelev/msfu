from django.shortcuts import render_to_response
from .models import Tag
# Create your views here.

def tag_list(request, **kwargs):
    context = kwargs['base_context']
    context['tags'] = Tag.objects.all()
    return render_to_response('list_tags.html', context)