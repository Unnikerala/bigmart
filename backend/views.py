from django.shortcuts import render,redirect
from backend.models import elementdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import productdb
from backend.models import listdb
from django.contrib import messages


# .....................................................................................................

def categorypage(request):
    return render(request,'productlist.html')

def savecategory(request):
    if request.method=="POST":
        cn=request.POST.get('categoryname')
        d=request.POST.get('description')
        pic=request.FILES['img']
        obj=listdb(categoryname=cn,description=d,categorypic=pic)
        obj.save()
        messages.success(request,'Data Saved Sucessfully')
        return redirect(categorypage)

def displaycategory(request):
    data=listdb.objects.all()
    return render(request,'productlistdisplay.html',{'data':data})


def editcategory(request,cid):
    data=listdb.objects.get(id=cid)
    return render(request,'productlistedit.html',{'data':data})

def updatecategory(request,cid):
    if request.method=="POST":
        cn = request.POST.get('categoryname')
        d = request.POST.get('description')
        try:
            img = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=listdb.objects.get(id=cid).categorypic
        listdb.objects.filter(id=cid).update(categoryname=cn,description=d,categorypic=file)
        return redirect(displaycategory)

def deletecategory(request,cid):
    d=listdb.objects.filter(id=cid)
    d.delete()
    messages.error(request,'Deleted')
    return redirect(displaycategory)











# ......................................................................................................


def indexdata(request):
    return render(request,'index.html')

def adddata(request):
    data = listdb.objects.all()
    return render(request,'addcategory.html',{'data':data})



def savedata(request):
    if request.method=="POST":
        n = request.POST.get("name")
        e = request.POST.get("Category")
        p = request.POST.get("price")
        im = request.FILES["image"]

        obj = elementdb(name=n,Category=e,price=p,image=im)
        obj.save()
        return redirect(adddata)



def displaydata(request):
    data = elementdb.objects.all()
    return render(request,'displaycategory.html', {"data":data})


def editdata(request, eleid):
    data = elementdb.objects.get(id=eleid)
    cat = listdb.objects.all()
    return render(request,'editcategory.html',{'data':data, 'cat':cat})


def updatedata(request,eleid):
    if request.method=="POST":
        n = request.POST.get("name")
        e = request.POST.get("Category")
        p = request.POST.get("price")

        try:
            y= request.FILES["image"]
            x = FileSystemStorage()
            file = x.save(y.name,y)
        except MultiValueDictKeyError:
            file = elementdb.objects.get(id=eleid).image
        elementdb.objects.filter(id=eleid).update(name=n,Category=e,price=p,image=file)

        return redirect(displaydata)


def deletedata(request,eleid):
    x = elementdb.objects.filter(id=eleid)
    x.delete()
    return redirect(displaydata)










# --------------------------------------------------------------------------------------------------------------
def displaycontact(request):
    data = productdb.objects.all()
    return render(request,'contactpage.html',{'data':data})

def deletecontact(request,proid):
    y = productdb.objects.filter(id=proid)
    y.delete()
    return redirect(displaycontact)


# ...........................................................................................


def loginpage(request):
    return render(request,'admin.html')

def adminlogin(request):
    if request.method=="POST":
        u = request.POST.get('user')
        p = request.POST.get('password')
        if User.objects.filter(username__contains=u).exists():
            y = authenticate(username=u,password=p)
            if y is not None:
                login(request,y)
                request.session['username']=u
                request.session['password']=p
                messages.success(request,'Welcome')
                return redirect(indexdata)
            else:
                messages.success(request,'Password Wrong')

                return redirect(loginpage)
        else:
            messages.success(request, 'User Not Found')

            return redirect(loginpage)


def logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,'Logged Out')

    return redirect(loginpage)

# .........................................................................................