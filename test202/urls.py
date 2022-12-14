from django.contrib import admin

from django.urls import path, re_path, include

from .views import home_page, contact_page, list_user, update, updaterecord, delete, register_page, quiz
from accounts.views import RegisterView, login_page
from products.views import ProductListView, ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView, ProductDetailSlugView
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static

from carts.views import cart_home


urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page),
    path('quiz/', quiz, name='quiz'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', list_user, name='list_user'),
    path('update/<int:id>', update, name='update'),
    path('products/', include("products.urls", namespace='products')),
    path('search/', include("search.urls", namespace='search')),
    path('delete/<int:id>', delete, name='delete'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('login/', login_page, name='login'),
    path('admin/', admin.site.urls),
    path('cart/', include("carts.urls", namespace='cart')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)