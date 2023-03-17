import requests
# Create your views here.
from django.shortcuts import render, HttpResponse
from FirstProgramme.models import UserInfo
from hashlib import md5


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


def md5_encrypt(pwd: str):
    salt = 'dnkjsna234adfa./'
    method = md5(salt.encode('utf8'))
    method.update(pwd.encode("utf8"))
    encrypt_pwd = method.hexdigest()
    return encrypt_pwd


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        email = request.POST.get('email')
        info = UserInfo.objects.filter(email=email).first()
        if info.email != '':
            return render(request, 'register.html', {"msg": "This email is already exists"})
        UserInfo.objects.create(email=email,
                                password=md5_encrypt(request.POST.get('password')),
                                age=request.POST.get('age'))
        return HttpResponse("done")
