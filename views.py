from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the TapBox</h1> <h1>Battery Status: </h1> <h1>Reset</h1> <h1>Logs: </h1> Previous Unlocks")
     

def detail(request, question_id):
    return HttpResponse("The battery level is %s" % question_id)
