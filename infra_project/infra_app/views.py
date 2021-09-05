from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница')
