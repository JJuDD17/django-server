from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

a = 0
def index(request):
    global a
    a += 1
    with open('./static/index.html') as file:
        return HttpResponse(file.read())

def work(request: WSGIRequest):
    text = request.GET.get('data')
    return HttpResponse(f'text is {text}')