from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Reservation

# Create your views here.
def index(request):
    #return HttpResponse('예약사이트')
    return render(request, 'reservation/index.html')

def reservation(request):
    return render(request, 'reservation/reservation.html')

def check(request, id):
    rlist = get_object_or_404(Reservation, pk=id)
    context = {'rlist': rlist}
    return render(request, 'reservation/list.html', context)

def enter(request):
    return render(request, 'reservation/enter.html')

def enterCheck(request):
    q = get_object_or_404(Reservation, name=request.POST.get('name'), phoneNumber=request.POST.get('phoneNumber'))
    context = {'id': q}
    return render(request, 'reservation/enterqr.html', context)

def create(request):
    r = Reservation(name=request.POST.get('name'), phoneNumber=request.POST.get('phoneNumber'), schoolName=request.POST.get('schoolName'), gradeNumber=request.POST.get('gradeNumber'))
    r.save()
    return redirect('reservation:check', id=r.id)