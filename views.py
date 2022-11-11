from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the TapBox index")

def detail(request, question_id):
    return HttpResponse("The battery level is %s" % question_id)