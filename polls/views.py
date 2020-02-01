from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.template import loader
from .models import Question

from string import ascii_letters
from random import randint, choice

ascii_letters += ',.:; '
def index(request: WSGIRequest):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls\index.html')
    context = {
        'latest_question_list': latest_question_list,
        #'comments': [''.join([choice(ascii_letters) for letter in range(randint(10, 80))]) for comment in range(randint(2, 15))]
    }
    return HttpResponse(template.render(context, request))
