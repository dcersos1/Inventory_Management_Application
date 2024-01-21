from django.db import models

# Create your models here.

#To keep data of registered users
#Primary key is the user id which is specific to each registered user and is auto generated
class Users(models.Model):
    User_Id = models.CharField(primary_key=True, max_length=200)
    Username = models.CharField(max_length=200, unique=True)
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)

#To keep data for current product inventory
#Primary key is the product id since this is unqiue to each specific product and the username is of the user who last altered the product
#Foreign keys of username and user id referencing values from User table
class Product_Inv(models.Model):
    Product_Id = models.IntegerField(primary_key=True)
    Product_Name = models.CharField(max_length=200)
    Product_Description = models.CharField(max_length=200)
    Product_Quantity = models.IntegerField()
    Prodcut_Price = models.IntegerField()
    Username = models.ForeignKey(Users, on_delete=models.CASCADE, to_field="Username", related_name="Username_Product_Inv")
    User_Id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="User_Id_Product_Inv")

#To keep data for user alterations
#Primary key is the time stamp since this is unique to each specific alteration 
#Foreign keys of user id and username referencing the Users table as well as a foregin key for product id referencing product inventory table
#Is not used in the project due to time constraints however this idea was in place. 
class Alterations(models.Model):
    User_Id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="User_Id_Alterations")
    Username = models.ForeignKey(Users, on_delete=models.CASCADE, to_field="Username", related_name="Username_Alterations")
    Product_Id = models.ForeignKey(Product_Inv, on_delete=models.CASCADE)
    Time_Stamp = models.DateTimeField(primary_key=True)

    