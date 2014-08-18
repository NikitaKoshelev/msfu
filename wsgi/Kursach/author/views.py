from django.shortcuts import render_to_response
from .models import Author


def list_authors(request, **kwargs):
    context = kwargs['base_context']
    context['authors'] = Author.objects.all()
    return render_to_response('list_authors.html', context)