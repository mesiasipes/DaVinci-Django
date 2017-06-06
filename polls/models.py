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
class Question(models.Model):
    name = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll)

    def __str__(self):
        return 'Question {}'.format(self.name)

@python_2_unicode_compatible
class Answer(models.Model):
    user_name = models.CharField(max_length=100)
    question = models.ForeignKey(Question)

    def __str__(self):
        return 'Answer {}'.format(self.name)
