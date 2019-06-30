## Winterfell Dry Cleaners Web App Development
Winterfell Dry Cleaners is the biggest dry cleaning shop in town. They are very busy these
days and need to improve their IT systems. Last month, they began development of a new
web app and need your help building a component.
In the past, staff wrote down a list of items a customer brought in for cleaning. They then
handed the customer a piece of paper with an order number on it so they could identify the
order upon collection.
This process has been replaced with a new system that stores this information in a
database. You can see the schema in the section below. You will need to recreate the
database using this information.
Staff members want to be able to look up an order by ID and print an invoice to give to the
customer. Your job is to build this page for the new app.
It needs to have the following functionality and design elements:
Allow staff to enter an order ID and press a submit button.
The page will then show the the following information for the matching order:
i. Customer name
ii. Order date
iii. Line item table
iv. VAT breakdown table
The item table should have the below four columns. Show the total of all lines as the
last row.
i. Item name
ii. Item price
iii. Quantity
iv. Line total
All prices include VAT so a VAT breakdown needs to appear below the item table. It
should have three columns:
i. Total excluding VAT
ii. VAT charged at 20%
iii. Total including VAT

### Basic Installation
*
1. Install pip
```bash
$ sudo apt-get install python-pip
```

2. Update pip to latest version (using sudo with pip requires the -H flag)
```bash
$ sudo -H pip install --upgrade pip
```

3. Install Django
```bash
$ pip install django
```

4. Download Dry cleaners app from Github repo. 

5. Edit the following lines of drycleaners/settings.py to match your environment

6. Create the application database
```bash
sudo python manage.py migrate
```

7. Create an admin user
```bash
sudo python manage.py create superuser
Username (leave blank to use 'root'): admin
Email address: admin@home.local
Password:
Password (again):
Superuser created successfully.
```

8. At this point, you should have enough configured to run the app using Python's development server. Run the following command and browse to http://localhost:8000
```bash
sudo python manage.py runserver 
```


### Using MySQL instead of SQLite3
1. Install MySQL client and Python MySQL driver
```bash
$ sudo apt-get install mysql-client
$ sudo -H pip install mysql-python
```

2. Create the MySQL database and user
```bash
$ mysql -u root -p [-h servername]
```
```sql
create database 'drycleaners';
grant all on 'drycleaners'.* to 'drycleaners'@'%' identified by 'mysecretpassword';
exit;
```

3. Update drycleaners/settings.py. 
```python


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'drycleaners',
        'USER': 'drycleaners',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'servername',
        'PORT': '',
    }
}
```
