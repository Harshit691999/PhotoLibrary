from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import os
from .forms import RegisterUser
from django.contrib.auth.models import User  # user is a inbulit model in djagno
from django.contrib.auth import authenticate,login,logout
from .decoraters import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@check_authenticated
def registeruser(request):
    form = RegisterUser()
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user = user,
            )
            return redirect('/')
    context = {"form":form,}
    return render(request,'registeruser.html',context)  

@check_authenticated
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')   

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("USEr : ",user)
            login(request,user)
            return redirect('userpage')
        else:
            print("back to log in page")
            return render(request,'login.html')
    return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return render(request,'login.html')

# hoem page -> changed to user page see below
def gallary(request):
    if request.user.is_anonymous:
        return redirect("loginuser")
    category = request.GET.get('category')
    categories = Category.objects.all()
    if category==None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__cat_name__contains=category)    
    # photos = Photo.objects.all()
    context = {
        "categories":categories,
        "photos":photos,
    }
    print(os.path)
    return render(request,'base.html',context)
    #return HttpResponse("<h1>hello{{request.user}} please login</h1>")

# @login_required('/loginuser')

def userpage(request):
    if request.user.is_anonymous:
        return redirect("loginuser")
    #photo = request.user.profile.photo_set.all()
    category = request.GET.get('category')
    categories = Category.objects.all()
    if category == None:
        photo = request.user.profile.photo_set.all()
    else:
        photo = request.user.profile.photo_set.filter(category__cat_name__contains=category)
    print(request.user)
    print("photo :",photo)
    #photo = current_user.photo_set.all()
    
    context = {
        "categories":categories,
        "photos":photo,
    }
    # print("photos: ",photo)
    return render(request,'userpage.html',context)

def viewphoto(request,pk):
    data = Photo.objects.get(id = pk)
    context = {
        "data":data,
    }
    return render(request,'viewphoto.html',context)

def addphoto(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form_data = request.POST      # its a form data through post request it is s dictionary of form posted data
        image = request.FILES.get('images')  # that is a image file 

        # print('data: ',form_data)
        # print('image: ',image)

        if form_data['category'] != 'none':
            category = Category.objects.get(id = form_data['category'])
        elif form_data['category_new'] != '':
            category , created = Category.objects.get_or_create(cat_name = form_data['category_new'])
        else:
            category = None
       
        photo = Photo.objects.create(
            profile = request.user.profile, # request user is the user object and we can access its field (request.user.filed_name)
            category=category,
            
            description=form_data['description'],
            image = image,
        )
        return redirect('userpage')
    context = {
        "categories":categories,
        #"photos":photos,
    }
    return render(request,'add.html',context)

def deleteimage(request,pk):
    data = Photo.objects.get(id = pk)
    if request.method == "POST":
        data.delete()
        if len(data.image)>0:
            os.remove(data.image.path)
        # if os.path.exists(data.image.name):
        #     os.remove(data.image.path)
        return redirect('userpage')