from django.contrib import admin
from Assignment_4_App.models import Users
from Assignment_4_App.models import Product_Inv
from Assignment_4_App.models import Alterations

# Register your models here.
admin.site.register(Users)
admin.site.register(Product_Inv)
admin.site.register(Alterations)
