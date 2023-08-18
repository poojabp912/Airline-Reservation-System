from django.shortcuts import render,redirect
from airline.models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Sum
import random

# jkdjwejdn
def home(request):
    return render(request,'index.html')

def adminl(request):
  if request.method=='POST':  
    email = request.POST['email']
    password=request.POST['password']
    if User.objects.filter(email=email,password=password).exists():
        return redirect('/lists')
    else :
        messages.success(request,'Invalid Email And Password!...')
        return redirect('/adminl')
  return render(request,'adminl.html')


def Insertrecord(request):
    if request.method=='POST':
        name = request.POST.get('name')  
        password = request.POST.get('password')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        date = request.POST.get('date')
        phno = request.POST.get('phno')
        if EmpInsert.objects.filter(email=email).exists():
            messages.error(request,'Email already exists..!')
            return redirect('/sign')
        else:
            EmpInsert(name=name,password=password,email=email,gender=gender,date=date,phno=phno).save()
            return redirect('/login')
    else:
        return render(request,'airsign.html')

def books(request,id):
    fly = fli.objects.get(id=id)
    obj = book.objects.filter(fid_id=id).aggregate(Sum('seats'))
    ob = book.objects.filter(fid_id=id).aggregate(su=Sum('seats'))
    if request.method=='POST':
            name = request.POST.get('name')  
            sour = request.POST.get('sour')
            dest = request.POST.get('dest')
            email = request.POST.get('email')
            price = request.POST.get('price')
            pay = request.POST.get('pay')
            date = request.POST.get('date')
            seats = request.POST.get('seats')
            eid_id = request.POST.get('eid_id')
            fid_id = request.POST.get('fid_id')
            rand = random.randint(0,100000)
            request.session['fid_id']=fid_id
            request.session['rand']=rand
            if ob['su'] is not None:
             obje = ob['su'] + int(seats)
             if obje > fly.seat:
              messages.error(request,'Sorry '+seats + ' seats are not available !')
              return redirect('/search')
             else:
              book(name=name,sour=sour,dest=dest,email=email,date=date,price=price,pay=pay,eid_id=eid_id,fid_id=fid_id,rand=rand,seats=seats).save()
              context = {"fly":fly,"obj":obj}
              return redirect('/rando',context)
            else:
             if int(seats) > fly.seat:
              messages.error(request,'Sorry '+seats + ' seats are not available !')
              return redirect('/search')
             else:
              book(name=name,sour=sour,dest=dest,email=email,date=date,price=price,pay=pay,eid_id=eid_id,fid_id=fid_id,rand=rand,seats=seats).save()
              context = {"fly":fly,"obj":obj}
              return redirect('/rando',context)
    return render(request,'book.html',{"fly":fly,"obj":obj})

def bdet(request,id):
    obje = book.objects.get(rand=id)
    return render(request,'bdet.html',{'dataa':obje})

def feedb(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try : 
         Userd = EmpInsert.objects.get(email=request.POST['email'],password=request.POST['password'])
         request.session['email'] = Userd.email
         eid_id = request.POST.get('eid_id')
         request.session['password'] = Userd.password
         feedba = request.POST.get('feedba')
         rating = request.POST.get('rating')
         Feedbac(email=email,password=password,feedba=feedba,rating=rating,eid_id=eid_id).save()
         return redirect('/')
        except EmpInsert.DoesNotExist as e:
            messages.success(request,'Invalid Email And Password!.')
    return render(request,'feedb.html')

def addf(request):
    if request.method=='POST':
        if request.POST.get('fname') and request.POST.get('sour') and request.POST.get('dest') and request.POST.get('price') and request.POST.get('seat'):
            fname = request.POST.get('fname')  
            sour = request.POST.get('sour')
            dest = request.POST.get('dest')
            price = request.POST.get('price')
            seat = request.POST.get('seat')
            fli(fname=fname,sour=sour,dest=dest,price=price,seat=seat).save()
            return redirect('/lists')
    else:
        return render(request,'addfli.html')

def lists(request):
    obj = fli.objects.all()
    return render(request,'flist.html',{"data":obj})

def bookv(request):
    ob = book.objects.all()
    return render(request,'bookv.html',{"data":ob})

def feedbv(request):
    obj = Feedbac.objects.all()
    return render(request,'feedbv.html',{"dat":obj})

# def new(request,id):
#     obj = book.objects.filter(fid_id=id).aggregate(Sum('seats'))
#     ob = fli.objects.get(id=id)
#     # print(obj)
#     return render(request,'new.html',{"dat":obj,'ob':ob})

def users(request):
    objec = EmpInsert.objects.all()
    return render(request,'users.html',{"dataa":objec})

def delete(request,id):
    obj = fli.objects.get(id =id)
    obj.delete()
    return redirect('/lists')
def delet(request,id):
    obje = EmpInsert.objects.get(id=id)
    obje.delete()
    return redirect('/users')
def deleted(request,id):
    obje = Feedbac.objects.get(id=id)
    obje.delete()
    return redirect('/feedbv')
def deleteb(request,id):
    obje = book.objects.get(id=id)
    obje.delete()
    return redirect('/bookv')

def search(request):
    if request.method=='POST':
        sour = request.POST.get('sour')
        dest = request.POST.get('dest')
        searc = fli.objects.raw('select * from flights where sour="'+sour+'" and dest="'+dest+'" ')
        return render(request,'search.html',{"data":searc})
    else:
        obj = fli.objects.all()
        return render(request,'search.html',{"data":obj})

def login(request):
    if request.method=='POST':
        try:
            Userd = EmpInsert.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("name=",Userd)
            print("gender=",Userd)
            print("password=",Userd)
            print("phno=",Userd)
            print("id=",Userd)
            request.session['email'] = Userd.email
            request.session['name'] = Userd.name
            request.session['password'] = Userd.password
            request.session['gender'] = Userd.gender
            request.session['phno'] = Userd.phno
            request.session['id'] = Userd.id
            return redirect('/search')
        except EmpInsert.DoesNotExist as e:
            messages.success(request,'Invalid Email And Password!.')
    return render(request,'ulogin.html')

def profi(request,id):
    obje = EmpInsert.objects.get(id=id)
    return render(request,'prof.html',{"dataa":obje})

def rand(request):
    obje = book.objects.filter(email=request.session["email"])
    ob = book.objects.all()
    return render(request,'rand.html',{'obje':obje,'ra':ob})

def rando(request):
    # obj = book.objects.filter(fid_id=request.session.fid_id).aggregate(Sum('seats'))
    # ob = fli.objects.get(id=request.session.fid_id)
    return render(request,'rando.html')

def upda(request, id):
    obje = EmpInsert.objects.get(id = id)
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('password') and request.POST.get('email') and request.POST.get('gender') and request.POST.get('date') and request.POST.get('phno') and request.POST.get('id'):
         try:
            saverecord = EmpInsert()
            saverecord.name = request.POST.get('name')  
            saverecord.password = request.POST.get('password')
            saverecord.email = request.POST.get('email')
            saverecord.gender = request.POST.get('gender')
            saverecord.date = request.POST.get('date')
            saverecord.id = request.POST.get('id')
            saverecord.phno = request.POST.get('phno')
            saverecord.save()
            return render(request,'index.html')
         except:
            messages.success(request,'Invalid Email And Password!.')
    else:
        return render(request,'upda.html',{"dataa":obje})

def update(request, id):
    obj = fli.objects.get(id =id)
    if request.method=='POST':
        if request.POST.get('fname') and request.POST.get('sour') and request.POST.get('dest') and request.POST.get('price'):
            saverecord = fli()
            saverecord.fname = request.POST.get('fname')  
            saverecord.id = request.POST.get('id')
            saverecord.sour = request.POST.get('sour')
            saverecord.dest = request.POST.get('dest')
            saverecord.price = request.POST.get('price')
            saverecord.seat = request.POST.get('seat')
            saverecord.save()
            return redirect('/lists')
    else:
        return render(request,'update.html',{"data":obj})

def logout(request):
    try:
        del request.session['email']
    except :
        return render(request,'index.html')
    return render(request,'index.html')
    

    






