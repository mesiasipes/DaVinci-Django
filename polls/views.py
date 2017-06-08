# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from polls.forms import UserResponseForm

from polls.models import Answer, Poll, UserResponse

def home(request):
    form = UserResponseForm()

    context = {
        'text' : 'this is my text',
        'polls' : Poll.objects.all(),
        'form': form,
    }

    return render(request, 'base.html', context)