import json
from datetime import datetime, timedelta

from django.db import models


class Person(models.Model):
    """
    Person Model.
    udid
    vehicle - null=True
    eta
        on new person creation
        create a new election
    """
    udid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    eta = models.DateTimeField(null=True, blank=True)
    boarded = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.udid)

    def save(self, *args, **kwargs):
        """
        on new person creation
        create a new election
        """
        super(Person, self).save(*args, **kwargs)

    def json(self):
        election = None
        try:
            elections = Election.objects.filter(result=None)
            if len(elections) > 0:
                election = elections[0]
        except:
            pass
        return json.dumps({
            'udid': self.udid,
            'eta': str(self.eta),
            'election': election.json(), })


class Election(models.Model):
    """
    election
        date_closed
        person - the new rider
    """
    date_closed = models.DateTimeField()
    person = models.ForeignKey(Person, related_name='elections')
    result = models.NullBooleanField(help_text='true if passenger voted on')
    yes_votes = models.IntegerField(null=True, blank=True)

    @property
    def closed(self):
        return self.date_closed <= datetime.utcnow()

    def vote_yes(self):
        self.yes_votes += 1

    def vote_no(self):
        self.yes_votes -= 1

    def save(self, *args, **kwargs):
        if self.id is None:
            now = datetime.utcnow()
            ending = now + timedelta(seconds=30)
            self.date_closed = ending
            total_riders = Person.objects.filter(boarded=True).count()
            self.yes_votes = total_riders
        super(Election, self).save(*args, **kwargs)
