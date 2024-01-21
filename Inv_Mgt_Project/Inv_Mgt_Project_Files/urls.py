"""
URL configuration for Assignment_4_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Assignment_4_App import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.Show_Product_Inv, name=''),
    path("InsertProducts", views.InsertProducts, name="InsertProducts"),
    path("Register", views.Register, name="Register"),
    path("Delete/<int:Product_Id>", views.del_products, name="del_products"),
    path("Delete/<str:User_Id>", views.del_user, name="del_user"),
    path("edit/<int:Product_Id>", views.Edit_Product, name="Edit_Product"),
    path("Update/<int:Product_Id>", views.update_product, name="update_product")
]
