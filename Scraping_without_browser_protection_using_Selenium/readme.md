# How to run 
    $ pip install selenium
    $ pip install SQLAlchemy
    $ python main.py

# how everything works together

## main.py
it manages every file

## database.py
first we need to create a connection with MySql server
for this purpose i'm using sqlalchemy
SQLAlchemy is an Object Relational Mapper (ORM) tool for Python. It is used to map Python objects to relational database tables and vice versa

## model.py
products class defines a table named "products" in the database with the tablename property.

## webScraping.py
this will scrape the html page and return the result
i have also created a ipynb file so you can check selenium.ipynb file.

