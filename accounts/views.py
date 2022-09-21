from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from .models import User
from accounts.forms import RegisterForm, LoginForm




def login_page(request):
    form = LoginForm(request.POST or None)
    regForm = RegisterForm(request.POST or None)
    # print(form)
    # print(request.user.is_authenticated)
    if request.POST and form.is_valid():
        user = form.login(request)
        print("test")
        print(user)
        if user:
            login(request, user)
            return redirect('home')
    if request.POST and regForm.is_valid():
        print(regForm.cleaned_data)
        print("test")

        email = regForm.cleaned_data.get("email")
        first_name = regForm.cleaned_data.get("first_name")
        last_name = regForm.cleaned_data.get("last_name")
        password = regForm.cleaned_data.get("password1")
        print(password)
        newUser = User.objects.create_user(email, password,first_name, last_name)
        print("test")
        print(email)
        print(newUser)
    context = {
        "form": form,
        "regForm": regForm
    }

    return render(request, "auth/login.html", context)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '/'



