"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from orders import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', views.CustomerList.as_view(), name="getpostcustomer"),
   # path('customers/<int:pk>/', views.CustomersListUpdate.as_view(), name='editcustomer'),
    path('products/', views.ProductList.as_view(), name="getpostproducts"),
#    path('products/<int:pk>/', views.ProductListUpdate.as_view(), name='editproducts'),
    path('orders/', views.OrderList.as_view(), name="getpostorder"),
 #   path('orders/<int:pk>/', views.OrderListUpdate.as_view(), name='editorder'),
    path("users/", views.UserCreate.as_view(), name="user_create"),
    path("login/", views.LoginView.as_view(), name="login"),
]


urlpatterns = format_suffix_patterns(urlpatterns)