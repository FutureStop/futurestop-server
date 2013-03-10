from datetime import datetime, timedelta
import json

from django.http import HttpResponse, HttpResponseBadRequest

from models import Person, Election


def udid(request, udid=None):
    if request.method == 'POST':
        import ipdb; ipdb.set_trace()
        try:
            data = json.loads(request.body)
            eta = int(data['eta'])
        except KeyError:
            return HttpResponseBadRequest('missing udid')
        end_eta = datetime.utcnow() + timedelta(seconds=eta)
        try:
            person, created = Person.objects.get_or_create(
                udid=udid, eta=end_eta, boarded=False)
        except Exception as e:
            return HttpResponseBadRequest('failed to create Person {0}'.format(
                str(e)))
    else:
        try:
            person = Person.objects.get(udid=udid)
        except:
            return HttpResponseBadRequest('missing Person')
    return HttpResponse(person.json())


def election(request):
    e = Election.objects.all()
    print e
    pass
