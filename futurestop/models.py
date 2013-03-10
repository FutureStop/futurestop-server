from django.db import models


class Vehicle(models.Model):
    """
    Vehicle Model.
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)


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
    vehicle = models.ForeignKey(Vehicle, related_name='passengers')
    #eta = models.IntegerField()
    eta = models.DateTimeField()

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
    vehicle = models.ForeignKey(Vehicle, related_name='elections')
    person = models.ForeignKey(Person, related_name='elections')
    result = models.NullBooleanField(help_text='true if passenger voted on')
    is_closed = models.BooleanField(default=False)
    yes_votes = models.IntegerField()

    @property
    def closed(self):
        # if current_time > date_closed
        return True

    def vote_yes(self):
        self.yes_votes += 1

    def save(self, *args, **kwargs):
        super(Election, self).save(*args, **kwargs)
