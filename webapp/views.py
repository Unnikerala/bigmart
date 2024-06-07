from django.shortcuts import render,redirect
from backend.models import elementdb,listdb
from webapp.models import productdb,registerdb,cartdb
from django.contrib import messages



def homepage(request):
    cat = listdb.objects.all()
    return render(request,'home.html',{'cat':cat})


def aboutpage(request):
    cat = listdb.objects.all()
    return render(request,'about.html',{'cat':cat})

def contactpage(request):
    cat = listdb.objects.all()

    return render(request,'contact.html',{'cat':cat})

def productpage(request):
    pro = elementdb.objects.all()
    cat = listdb.objects.all()

    return render(request,'products.html', {'pro':pro,'cat':cat})


def saveproduct(request):
    if request.method=="POST":
        n = request.POST.get("name")
        e = request.POST.get("email")
        s = request.POST.get("subject")
        m = request.POST.get("message")

        obj = productdb(name=n,email=e,subject=s,message=m)
        obj.save()
        return redirect(contactpage)


def filtered(request,cat_name):
    data = elementdb.objects.filter(Category=cat_name)
    cat = listdb.objects.all()
    return render(request,'productfiltered.html',{'data':data,'cat':cat})


def singleproduct(request,pro_name):
    data = elementdb.objects.get(id=pro_name)
    cat = listdb.objects.all()
    return render(request,'singleproduct.html',{'data':data,'cat':cat})




def registerpage(request):
    return render(request,'register.html')


def saveregister(request):
    if request.method=="POST":
        us = request.POST.get("user")
        em = request.POST.get("email")
        pa = request.POST.get("pass")
        obj = registerdb(Username=us,Email=em,Password=pa)
        obj.save()
        return redirect(registerpage)


def userlogin(request):
    if request.method=="POST":
        un = request.POST.get("uname")
        pwd = request.POST.get("password")
        if registerdb.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            messages.success(request, 'Welcome')
            return redirect(homepage)


        else:
            messages.success(request, 'Password Wrong')
            return redirect(registerpage)
    else:
        messages.success(request, 'User Not Found')
        return redirect(registerpage)


def logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request,'Logged Out Succesfully')

    return redirect(homepage)


def cartsave(request):
    if request.method=="POST":
        un = request.POST.get("username")
        pn = request.POST.get("productname")
        qn = request.POST.get("quantity")
        tp = request.POST.get("totalprice")
        obj = cartdb(Username=un,Productname=pn,Quantity=qn,Totalprice=tp)
        obj.save()
        messages.success(request,"SUCessfully Added to cart")
        return redirect(homepage)






def cartpage(request):
    data=cartdb.objects.filter(Username=request.session['Username'])
    cat = listdb.objects.all()
    total=0
    for d in data:
        total=total+d.TotalPrice
    if total>500:
        delivery_charge=0
    else:
        delivery_charge=50
    final=total+delivery_charge
    return render(request,"cart.html",{'cat':cat,'data':data,'total':total,'delivery_charge':delivery_charge,'final':final})


def delete_item(req,pid):
    x=cartdb.objects.filter(id=pid)
    x.delete()
    messages.error(req,"Deleted successfully")
    return redirect(cartpage)

def user_login_page(request):
    return render(request,"userlogin.html")


