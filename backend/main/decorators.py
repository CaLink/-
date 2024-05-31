import sys, os
from main.models import Analytics, Logs
from django.http import HttpResponse

def send_some_analytics(function):
    def wrap(request, *args, **kwargs):
        Analytics.objects.create(action=function.__name__)
        return function(request, *args, **kwargs)
    return wrap

def logging(function):
    def wrap(request, *args, **kwargs):
        try:
            return function(request, *args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            Logs.objects.create(type=e, file=fname, row=exc_tb.tb_lineno)
            return HttpResponse(status=400)
    return wrap