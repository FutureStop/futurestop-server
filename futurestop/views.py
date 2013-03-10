import json

from django.http import HttpResponse, HttpResponseBadRequest

from models import Person, Election


def udid(request, udid=None):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except KeyError:
            return HttpResponseBadRequest('missing udid')
        created, person = Person.objects.get_or_create(udid=udid)
    return HttpResponse('udid {0}'.format(udid))


def election(request):
    pass
