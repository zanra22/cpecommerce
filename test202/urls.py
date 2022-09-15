from django.contrib import admin
from django.urls import path

from .views import home_page, contact_page, list_user, update, updaterecord, delete
from accounts.views import RegisterView, login_page

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', list_user, name='list_user'),
    path('update/<int:id>', update, name='update'),

    path('delete/<int:id>', delete, name='delete'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('login/', login_page, name='login'),
    path('admin/', admin.site.urls),
]
