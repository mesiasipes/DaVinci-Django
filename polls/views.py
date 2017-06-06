# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from polls.models import Answer, Poll, Question

def home(request):
    context = {
        'text' : 'this is my text',
        'polls' : Poll.objects.all(),
    }
    return render(request, 'base.html', context)