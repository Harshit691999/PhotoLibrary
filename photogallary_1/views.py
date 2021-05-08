from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import os
# Create your views here.

def gallary(request):
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

def viewphoto(request,pk):
    data = Photo.objects.get(id = pk)
    context = {
        "data":data,
    }
    return render(request,'viewphoto.html',context)

def addphoto(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form_data = request.POST      # its a form data through post request
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
            category=category,
            
            description=form_data['description'],
            image = image,
        )
        return redirect('/')
    context = {
        "categories":categories,
        #"photos":photos,
    }
    return render(request,'add.html',context)

def deleteimage(request,pk):
    data = Photo.objects.get(id = pk)
    if request.method == "POST":
        data.delete()
        # if len(data.image)>0:
        #     os.remove(data.image.path)
        if os.path.exists(data.image.name):
            os.remove(data.image.path)
        return redirect('/')