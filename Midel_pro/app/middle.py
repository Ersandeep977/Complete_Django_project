from django.http import HttpResponse
class sandeepmid(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return HttpResponse('<h1>hello Sandeep plze meet me 2 days !!!!')