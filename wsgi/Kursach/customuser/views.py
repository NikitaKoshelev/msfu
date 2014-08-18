# coding=utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth
from django.contrib.auth.models import Group

from .models import CustomUser
from customuser.forms import CustomUserCreationForm


def create(request, **kwargs):
    context = kwargs['base_context']
    auth.logout(request)
    context['form'] = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            auth.login(request, user)
            context['user'] = user
            user_model = CustomUser.objects.get(username=form.cleaned_data['username'])
            user_model.is_staff = True
            group = Group.objects.get(name=u'Студенты')
            user_model.groups.add(group)
            user_model.save()
            messages.success(request, _(u'Welcome'))
            return HttpResponseRedirect('/')
        else:
            form = CustomUserCreationForm()
            context['form'] = form

    return render_to_response('registration/registration_form.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.path[:-len(u'аккаунты/Выход/')])