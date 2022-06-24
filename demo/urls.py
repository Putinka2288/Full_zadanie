from django.urls import path
from django.contrib.auth import views as auth_views
from demo import views
from demo.views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('validate_username', validate_username, name='validate_username'),
    path('validate_mail', validate_mail, name='validate_mail'),

    path('', catalog, name='catalog'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('product/<pk>', product, name='product'),

    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('orders', OrderListView.as_view(), name='orders'),
    path('delete_order/<pk>', delete_order, name='delete_order'),
    path('to_cart/<pk>', to_cart, name='to_cart'),

    path('to_cartMinus/<pk>', to_cartMinus, name='to_cartMinus')
    ]
