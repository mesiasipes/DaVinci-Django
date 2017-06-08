# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Poll(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return 'Poll {}'.format(self.name)

@python_2_unicode_compatible
class Answer(models.Model):
    name = models.CharField(max_length=100, null=True)
    poll = models.ForeignKey(Poll, null=True)

    def __str__(self):
        return 'Question {}'.format(self.name)

@python_2_unicode_compatible
class UserResponse(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    answer = models.ForeignKey(Answer, null=True)

    def __str__(self):
        return self.user_name
