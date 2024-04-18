from django.http import HttpResponse
from django.shortcuts import render
from procedure.models import *


# Create your views here.
def index(request):
    context={
        'title':'Авторизация'
    }
    return render(request, 'procedure/main.html',context=context)


def show(request):
    login = request.POST.get('username')
    password = request.POST.get('password')
    data = User.objects.all()

    iD = 0
    FIO = ''
    for i in data:
        if i.Login == login and i.Password == password:
            iD = i.pk
            FIO = i.FIO
        else:
            return HttpResponse('<h1>Неверный логин или пароль</h1>')
    b = Clients.objects.filter(FIO=iD)
    con = {
        'title': 'Клиенты',
        'clients': b,
        'FIO': FIO,
    }
    return render(request, 'procedure/show.html', context=con)


def up(request):
    stt=request.GET.get('stid')
    status=Status.objects.all()
    con = {
        'idcl': stt,
        'stat':status,
        'title':'Обновление статуса'
    }
    return render(request, 'procedure/update.html', context=con)
def send(request):
    idd=0
    status=request.POST.get('stAtus')
    iDc = request.POST.get('iDc')
    sr=Status.objects.filter(name=status)
    for i in sr:
        idd=i.pk
    client = Clients.objects.get(pk=iDc)
    client.status=Status.objects.get(pk=idd)
    client.save()
    return HttpResponse('<h1>Данные отправлены</h1>')