from django.urls import path, re_path
from .views import cart_home, cart_update
app_name = 'cart'
urlpatterns = [
    path('', cart_home, name='cart_home'),
    path('update/', cart_update, name='cart_update'),
]
