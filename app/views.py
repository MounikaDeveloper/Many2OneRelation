from django.contrib import messages
from django.shortcuts import render, redirect
from app.models import Biryani,BiryaniType
# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def addBiryaniType(request):
    n = request.POST.get("bt1")
    na = request.POST.get("bt2")
    BiryaniType(no=n, type=na).save()
    messages.success(request, "Biryani Type is Saved")
    return redirect('main')


def addBiryani(request):
    return render(request,"addbiryani.html",{"data":BiryaniType.objects.all()})


def saveBirani(request):
    a = request.POST.get("bt1")
    b = request.POST.get("bt2")
    c = request.POST.get("bt3")
    d = request.POST.get("bt4")
    Biryani(no=a, name=b, price=c, biryani_type_id=d).save()
    messages.success(request, "Biryani is Saved")
    return redirect('addb')


def view(request):
    bt=BiryaniType.objects.all()
    b=Biryani.objects.all()
    return render(request,"view.html",{"data1":bt,"data2":b})