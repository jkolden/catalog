# Catalog Project
Catalog Project for Udacity Full Stack Nanodegree.

This project is a python/flask application that supports CRUD operations against a sqlite database. The database contains items that might be stocked by a sporting goods store. The items can be filtered by category (Baseball, Football etc.) and the application allows users to add/edit/delete items as necessary. All changes to the data are persisted to the sqlite database using POST operations on the flask endpoints.

The database that this program queries contains three tables: user, categories and items. Categories and items have a foriegn key relationship to the user table, and items has a foriegn key relationship to the categories table.

The definitions of these tables is as follows:

### user table definition:
```
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
```

### categories table definition:
```
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
```

### items table definition
```
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    cat_id = Column(Integer, ForeignKey('categories.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    categories = relationship(Categories)
```

## How to run this code

### Install the VM and Vagrant:
This project uses a virtual machine (VM) to run a SQL database server.
1. If you don't already have virtual box on your machine, you can download it here:
- https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
2. Download and install Vagrant (if you do not already have it installed). This is the software that configures the VM and allows the host (your machine) to talk to the VM:
- https://www.vagrantup.com/downloads.html
- you should be able to run ```$ vagrant --version``` after installation to see the version that was installed.
3. Clone this repository: https://github.com/jkolden/catalog.git to a directory on your local machine and then cd into this directory.
4. cd into the vagrant subdirectory
5. Bring the VM up with the command ```vagrant up```
6. Log into the VM with ```vagrant ssh```

### Create and populate the database (not required):
1. This application will come with a prepopulated database named sportingequipment.db
2. If required for this assignment you can delete the sportingequipment.db file from the catalog subdirectory and recreate it by running the following commands at the command line:
- cd into the vagrant/catalog directory
- vagrant@vagrant:/vagrant/catalog$ python database_setup1.py
- vagrant@vagrant:/vagrant/catalog$ python categories.py 
- You should now see the sportingequipment.db file created inside your vagrant/catalog subdirectory.

### Run the project.py file
1. At the ```vagrant@vagrant:~$ ``` prompt, cd into: /vagrant/catalog.
2. In the /vagrant/catalog subdirectory run the project file:
- vagrant@vagrant:/vagrant/catalog$ python project.py
2. You can now access the running application on http://localhost:8000/

### How to use the application
1. The recommended browser is Google Chrome.
2. The application homepage provides a list of categories and their respective items.
3. Before you can perform any operations you will need to click the ```login``` link in the upper right corner.
- You can login with your google sign in.
- After successfully signing in you will be redirected to the catalog app homepage and your username will appear in the upper right corner.
4. Select a category on the left to see the items that are in that category. The items will be displayed on the right.
5. Select an item to see the details of that item.
6. Click the ```create new item``` link to add a new item. You will be recorded as the owner of the item and you will have priviledges to edit and/or delete this item as well.
7. To logout, simply click the ```logout``` link in the upper right corner.

### How to use this application's data with another application
1. This catalog app provides a JSON endpoint that can be consumed as a GET request in any other application.
2. The endpoint is http://localhost:8000/catalog.json/ and the response payload will be an object of all categories with an array of items belonging to that category.
