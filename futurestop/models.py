from django.db import models
from datetime import datetime, timedelta


#class Vehicle(models.Model):
#    """
#    Vehicle Model.
#    """
#    name = models.CharField(max_length=255)
#
#    def __unicode__(self):
#        return unicode(self.name)


class Person(models.Model):
    """
    Person Model.
    udid
    vehicle - null=True
    eta
        on new person creation
        create a new election
    """
    udid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    #vehicle = models.ForeignKey(Vehicle, related_name='passengers')
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


class Election(models.Model):
    """
    election
        date_closed
        vehicle
        new rider
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
