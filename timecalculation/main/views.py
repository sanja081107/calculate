from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datetime_safe import datetime

def home(request):
    return render(request, 'main/base.html')


def calculation(request):
    time_in = request.POST['time-in']
    time_out = request.POST['time-out']
    time_in_new = time_in.replace(' ', '')
    time_out_new = time_out.replace(' ', '')

    if time_in_new.isdigit() and time_out_new.isdigit():
        s1 = time_in.split(' ')
        s2 = time_out.split(' ')
        o1 = datetime(day=1, month=1, year=2023, hour=int(s1[0]), minute=int(s1[1]), second=int(s1[2]))
        o2 = datetime(day=1, month=1, year=2023, hour=int(s2[0]), minute=int(s2[1]), second=int(s2[2]))
        if o1 < o2:
            o = o2 - o1
            m = o / 60
            return HttpResponse(f"Ответ: <br>Минуты с секундами: {o}, <br>Только в минутах: {m}")
        else:
            return HttpResponse('Конечное время меньше чем начально')
    elif time_in == '' or time_out == '':
        return HttpResponse('Введите время')
    else:
        return HttpResponse('Неверный формат времени')
