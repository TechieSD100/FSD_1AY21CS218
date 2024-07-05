from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.
def current_datetime(request):
    now1 = datetime.now() - timedelta(hours=4)
    now2 = datetime.now() + timedelta(hours=4)
    html = "<html><body><br><h2 align=center>Current date and time 4hrs ago: {}<br><br>".format(now1)+"Current date and time 4hrs after: {}</h2></body></html>".format(now2)
    return HttpResponse(html)
