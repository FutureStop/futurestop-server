from django.http import HttpResponse

from models import Vehicle, Person, Election


def udid(request, udid=None):
    return HttpResponse('udid {0}'.format(udid))
