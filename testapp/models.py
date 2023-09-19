from django.contrib.auth.models import User
from django.db import models
from test_django_reversion.models import AuditAbstractModel


class Poll(AuditAbstractModel):
    """Model with history field"""
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(AuditAbstractModel):
    """Model without history field"""
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
