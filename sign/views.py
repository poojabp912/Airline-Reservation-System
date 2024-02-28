from django.shortcuts import render
from sign.models import EmpInsert
from django.contrib import messages

def Insertrecord(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('password') and request.POST.get('email') and request.POST.get('gender') and request.POST.get('date') and request.POST.get('phno'):
            saverecord = EmpInsert()
            saverecord.name = request.POST.get('name')  
            saverecord.password = request.POST.get('password')
            saverecord.email = request.POST.get('email')
            saverecord.gender = request.POST.get('gender')
            saverecord.date = request.POST.get('date')
            saverecord.phno = request.POST.get('phno')
            saverecord.save()
            messages.success(request,'Record Saved Successfully')
            return render(request,'airsign.html')
    else:
        return render(request,'airsign.html')