from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "admin_app/home.html", context)
    else:
        return render(request, "admin_app/home.html")

def admin(request):
    if 'user_id' in request.session:
        return redirect('/')
    else:
        return render(request, "admin_app/login.html")

def login(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value, extra_tags=key)
        print(errors)
        return redirect('/login')
    else:
        this_user = User.objects.filter(email=request.POST['email'])
        if len(this_user) > 0:
            request.session['user_id'] = this_user[0].id
            return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def about(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "admin_app/about.html", context)
    else:
        return render(request, "admin_app/about.html")


def services(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "admin_app/services.html", context)
    else:
        return render(request, "admin_app/services.html")

def shop(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "admin_app/shop.html", context)
    else:
        return render(request, "admin_app/shop.html")

def gallery(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id']),
            'images': Gallery.objects.all()
        }
    else:
        context={
            'images': Gallery.objects.all()
        }
    return render(request, "admin_app/gallery.html", context)

def upload(request):
    errors = Gallery.objects.basic_validator(request.FILES)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/gallery')
    else:
        if request.method == 'POST' and request.FILES['image']:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
            Gallery.objects.create(image=uploaded_file_url)
            # print(Gallery.objects.all().values())
        return redirect('/gallery')

def delete_img(request):
    Gallery.objects.get(id=request.POST['image_id']).delete()
    return redirect('/gallery')

def contact(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "admin_app/contact.html", context)
    else:
        return render(request, "admin_app/contact.html")