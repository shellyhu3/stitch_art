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
    print('info', request.POST)
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


def services(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "admin_app/services.html", context)
    else:
        return render(request, "admin_app/services.html")

def engraving(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "admin_app/engraving.html", context)
    else:
        return render(request, "admin_app/engraving.html")

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
            # uploaded_file_url = fs.url(filename)
            # Gallery.objects.create(image=uploaded_file_url)
            Gallery.objects.create(image=filename)
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


def account(request):
    if 'user_id' in request.session:
        context={
            'this_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "admin_app/account.html", context)
    else:
        return redirect('/')


def update(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value, extra_tags=key)
        print(errors)
        return redirect('/account')
    else:
        edit_user = User.objects.get(id=request.session['user_id'])
        if len(request.POST['old_pw']) < 1 and len(request.POST['new_pw']) < 1 and len(request.POST['confirm_new_pw']) <1:
            edit_user.email = request.POST['newEmail']
            edit_user.save()
            messages.success(request, "Successfully updated")
        else:
            edit_user.email = request.POST['newEmail']
            hashed_pw = bcrypt.hashpw(request.POST['new_pw'].encode(), bcrypt.gensalt())
            edit_user.password = hashed_pw.decode()
            edit_user.save()
            messages.success(request, "Successfully updated")
        return redirect('/account')