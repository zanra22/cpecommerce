from django.shortcuts import render, redirect
from django.views.generic import ListView

from products.models import Product
from .forms import ContactForm
from accounts.forms import RegisterForm

from django.contrib.auth import get_user_model
User = get_user_model()

def list_user(request):
    model = User.objects.all().values()
    # print(model)
    context = {
        'model': model
    }
    return render(request, 'auth/list_user.html', context)

def update(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'auth/update.html', context)

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('list_user')

def updaterecord(request, id):
    newEmail = request.POST['email']
    newFirstName = request.POST['first_name']
    user = User.objects.get(id=id)
    user.email = newEmail
    user.first_name = newFirstName
    user.save()
    return redirect('list_user')

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        newUser = User.objects.create_user(username, email, password)

    return render(request, "auth/register.html", context)


def home_page(request):
    # print("test")
    print(request.session.get("first_name", "Unknown"))
    list = Product.objects.all()
    context = {
        'list': list
    }
    return render(request, 'home_page.html', context)

def quiz(request):
    return render(request, 'quiz.html')

def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/contact.html", context)