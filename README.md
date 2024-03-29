# Inventory_Management_Application

Daniel Cersosimo - Full Stack Developer

Welcome to my Inventory Management Application! A description of the application and how to run it are provided below. I provided images to show the user interface and a glimpse into some of the features with sample products and users. Thank you for viewing and I hope you enjoy it. 

#Summary of my work

• Facilitated the design and execution of this application for unique users to be able to execute the necessary CRUD operations

• Support for specific manager login and random generated ID for enhanced documentation of user action upon the inventory

• Configured PostgreSQL as the database and leveraged the ORM of Django to migrate classes of Python objects to serve as tables

• Employed the Django REST framework to streamline the connection between the user interface and backend logic

• Utilized HTML for UI structure while incorporating CSS for enhanced display and functionality

#Explanation of functionality

This project creates an inventory management user interface which takes in user input for themselves and products while organizing this information into viewable tables. These tables are supported by a backend database, postgreSQL, which is connected to the project via a configuration in settings.py. These tables are initially designed in models.py and migrated over to the database following a successful configuration where they are materialized in postgreSQL. The following files in the django project are configured with respect to this database and this array of python and html files allow for the user end of a webpage to be connected to and predicated off of the database. This visualized front end is displayed on a webpage configured to localhost from which a user interacts with various pages with specific functionalities such as client registration and much more. These pages are designed by multiple HTML files and enhanced by with CSS. For each operation, the webpages are configured to take in user input which is communicated back to the backend in the python files such as views.py, urls.py, and more. These files are coded to interpret these requests and carry out each file's respective logic accordingly to support this inventory management system. 


#How to run the application 

In order to run this on another device, all the relevant files must be downloaded and opened. These files were generated via a startproject and startapp django-admin commands. Django and PostgreSQL must be installed, this project uses PGAdmin, and a database must be running and configured as seen in settings.py. Psycopg2 should be installed via pip install psycopg2. From this, a django migration, python manage.py migrate, for the models to the database must be enacted in order for the connection to be realized and another migration, python manage.py migrate --run-syncdb, to sync the models to the db must be run to transfer the models to become tables in the database. Following this, ensure any other necessary configurations are carried out and in place. These actions were executed via anaconda powershell. When this is all set up, issuing a command from manage.py in the shell to run the server, python manage.py runserver, can be executed to run the Inventory Management Application on a provided url on localhost. 


#Additional notes

• The models.py includes an alterations class which was migrated over to the database to be utilized to timestamp each alteration. Unfortunately, this project does not make use of this 
  supplemental feature due to time constraints which required me to adapt the project and ensure core components were attained on schedule. As a result, only the product and user tables 
  are utilized for the main functions of the inventory management system. The idea of how this was going to be done can be seen in the models file.

• The function to update product information in views.py was having issues with the usage of forms so I coded to manually carry out the update process and ensure the attempted updates 
  are valid. 

• There are additional comments in the views and models python files as well which provide detailed insight into the functionality and logic of the code.
