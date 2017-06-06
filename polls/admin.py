# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from polls.models import Answer, Question, Poll

admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(Question)

