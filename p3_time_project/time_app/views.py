from django.http import HttpResponse
from datetime import datetime


def current_datetime(request):
   now = datetime.now()
   html = "<html><body><h2 align=center>Current date and time: {}</h2></body></html>".format(now)
   return HttpResponse(html)
