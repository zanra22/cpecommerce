from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from .models import User
from accounts.forms import RegisterForm, LoginForm




def login_page(request):
    form = LoginForm(request.POST or None)
    # print(form)
    # print(request.user.is_authenticated)
    if request.POST and form.is_valid():
        user = form.login(request)
        print("test")
        print(user)
        if user:
            login(request, user)
            # success_url = reverse_lazy('login')
            # ontext['form'] = LoginForm()
            return redirect('home')
    context = {
        "form": form
    }

    return render(request, "auth/login.html", context)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '/'



