# How to run 
    $ pip install selenium
    $ pip install SQLAlchemy
    run main.ipynb file

# how everything works together

## main.ipynb
it manages every file and also does the scraping

## database.py
first we need to create a connection with MySql server
for this purpose i'm using sqlalchemy
SQLAlchemy is an Object Relational Mapper (ORM) tool for Python. It is used to map Python objects to relational database tables and vice versa

## model.py
products class defines a table named "products" in the database with the tablename property.



