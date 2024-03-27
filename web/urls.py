"""
URL configuration for loqz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views
app_name = "web"
urlpatterns = [
  path("",views.index,name="index"),
  path("about/",views.about,name='about'),
  path("product/",views.product,name='product'),
  path("contact/",views.contact,name='contact'),
  path('updates/',views.updates,name='updates'),
  path('product_details/<slug:slug>/',views.product_details,name='product_details'),
  path('update_details/<slug:slug>/',views.update_details,name='update_details'),
  path('dealership/',views.dealership,name='dealership'),

]
