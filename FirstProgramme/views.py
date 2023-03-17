import requests
# Create your views here.
from django.shortcuts import render, HttpResponse
from FirstProgramme.models import UserInfo


# def index(request):
#     return HttpResponse('welcome!')
#
#
# def user_list(request):
#     print(request.method)
#     print(request.POST)
#     name = 'mail'
#     age = '16'
#     role = ['保安', 'ceo', 'cfo']
#     return render(request, 'userList.html', {'n1': name, 'n2': age, 'n3': role})
#
#
# def news(request):
#     req = requests.get('https://www.runoob.com/python/python-install.html')
#     print(req.json())
#     return render(request, 'news.html', {'new': req.json()})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        a = UserInfo.objects.filter(email=email).first()
        if not a:
            return render(request, 'login.html', {'msg': 'This account does not exist'})
        elif a.password != pwd:
            return render(request, 'login.html', {'msg': 'The password is incorrect'})
        return HttpResponse('done')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        pass
