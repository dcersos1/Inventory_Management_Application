# Create your views here.

#Import the necessary modules, functions, and information
from django.shortcuts import render
from django.shortcuts import redirect
from Assignment_4_App.models import Product_Inv
from Assignment_4_App.models import Users
from Assignment_4_App.models import Alterations
from django.contrib import messages
from django.http import HttpResponse
import random

#Function for homepage to show the product table and user table
def Show_Product_Inv(request):
    Products = Product_Inv.objects.all()
    Users_1 = Users.objects.all()
    return render(request, 'Homepage.html', {'data':Products, 'user_data':Users_1})

#Function to randomly generate an id for the product that is unique to each product
def generate_random_product_id():
    characters = '0123456789'
    auto = ''.join(random.choice(characters) for i in range(4))
    auto = int(auto)
    return auto

#Function for the insert page to give the http request from the insert html functionality with the database 
#Also ensures that the attempted changes by a front end user are realized in the database with a message displayed for sucess and failure
def InsertProducts(request):
    if request.method == "POST":
        if request.POST.get('Product_Name') and request.POST.get('Product_Description') and request.POST.get('Product_Quantity') and request.POST.get('Prodcut_Price') and request.POST.get('User_Id_id') and request.POST.get('Username_id'):
            saverecord = Product_Inv()
            saverecord.Product_Id = generate_random_product_id()
            saverecord.Product_Name = request.POST.get('Product_Name')
            saverecord.Product_Description = request.POST.get('Product_Description')
            saverecord.Product_Quantity = request.POST.get('Product_Quantity')
            saverecord.Prodcut_Price = request.POST.get('Prodcut_Price')
            saverecord.Username_id = request.POST.get('Username_id')
            saverecord.User_Id_id = request.POST.get('User_Id_id')
            saverecord.save()
            messages.success(request, 'Product ' + saverecord.Product_Name + ' is saved successfully!')
        else:
            messages.error(request, 'Failed to save the Product. Please fill in all required fields.')
    return render(request, 'Insert.html')

#Function to generate a random user id that will be unique to each user
def generate_random_user_id():
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    auto = ''.join(random.choice(characters) for i in range(5))
    return auto

#Function to give the Register html page functionaility by allowing for front end users requests to be materialized in the database 
#Also ensures the user input is valid and can be saved to the database via confirmation messages
def Register(request):
    if request.method == "POST":
        if request.POST.get('Username') and request.POST.get('First_Name') and request.POST.get('Last_Name'):
            saverecord = Users()
            saverecord.Username = request.POST.get('Username')
            saverecord.First_Name = request.POST.get('First_Name')
            saverecord.Last_Name = request.POST.get('Last_Name')
            saverecord.User_Id = generate_random_user_id()
            saverecord.save()
            messages.success(request, 'Registration for ' + saverecord.Username + ' is successfull!')
        else:
            messages.error(request, 'Failed to register. Please fill in all required fields.')
    return render(request, 'Register.html')

#This provides a delete functionaility for delete option in the homepage to delete each product
def del_products(request, Product_Id):
    del_p=Product_Inv.objects.get(Product_Id=Product_Id)
    del_p.delete()
    return redirect("")

#This provides a delete functionaility for delete option in the homepage to delete each user
def del_user(request, User_Id):
    del_u=Users.objects.get(User_Id=User_Id)
    del_u.delete()
    return redirect("")

#This provides the edit option on the homepage with functionaility to then go to the edit page and support the display the information for the product there
def Edit_Product(request, Product_Id):
    edit_p = Product_Inv.objects.get(Product_Id=Product_Id)
    return render(request, 'edit.html', {"Product_Inv":edit_p})

    

#This provides the ability to update product information. This would typically use forms however there was an issue with this so I manually coded it
def update_product(request, Product_Id):
    prod = Product_Inv.objects.get(Product_Id=Product_Id)
    if request.method == 'POST':
        new_product_name = request.POST.get('Product_Name')
        new_product_description = request.POST.get('Product_Description')
        new_product_quantity = request.POST.get('Product_Quantity')
        new_product_price = request.POST.get('Prodcut_Price')
        new_username_id = request.POST.get('Username_id')
        new_user_id_id = request.POST.get('User_Id_id')

        #Ensure the data for quantity and price are integers
        new_product_quantity = int(new_product_quantity)
        new_product_price = int(new_product_price)
        # Check the product information and update if it clears all the conditions while returning sucess or failure messages
        while True:
            if isinstance(new_product_name, str):
                prod.Product_Name = new_product_name
            else:
                messages.error(request, "Failed to update. Please fill in the product name with a string and all fields with proper data type")
                break
            if isinstance(new_product_description, str):
                prod.Product_Description = new_product_description
            else:
                messages.error(request, "Failed to Update. Please fill in the product description with a string and all fields with the proper data type")
            if isinstance(new_product_quantity, int):
                prod.Product_Quantity = new_product_quantity
            else:
                messages.error(request, "Failed to update. Please fill in the product quantity with an integer and all fields with proper data type")
                break
            if isinstance(new_product_price, int):
                prod.Prodcut_Price = new_product_price
            else:
                messages.error(request, "Failed to update. Please fill in the product price with an integer and all fields with proper data type")
                break
            #This function checks if the username edit attempted by the user exists in the Users table
            def check_username(new_username_id):
                return Users.objects.filter(Username=new_username_id).exists()
            
            if check_username(new_username_id):
                prod.Username_id = new_username_id
            else:
                messages.error(request, "Failed to update. Please fill in the username with a registered username and all fields with proper data type")
                break
            #This function checks if the user id edit attempted by the user exists in the Users table
            def check_user(new_user_id_id):
                return Users.objects.filter(User_Id=new_user_id_id).exists()

            if check_user(new_user_id_id):
                prod.User_Id_id = new_user_id_id
            else:
                messages.error(request, "Failed to update. Please fill in the username with a registered user id and all fields with proper data type")
                break
            #Save and return sucess message if all conditions passed
            prod.save()
            messages.success(request, 'Product information is updated successfully.')
            break
    return render(request, 'edit.html', {'Product_Inv': prod})