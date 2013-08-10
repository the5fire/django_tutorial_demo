from django.http import HttpResponse

from polls.models import Poll


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)


def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
