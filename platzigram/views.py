"""Platigram views"""
from datetime import datetime
from django.http import HttpResponse

def hello_world(reques):
    return HttpResponse('Oh, hi! Current server time is: {now}'.format(
        now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    ))

def hi(request):
    # import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))