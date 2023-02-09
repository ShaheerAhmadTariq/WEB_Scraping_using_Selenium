from database import engine, SessionLocal
import model
from model import products
from webScraping import startWebScrapping
import pprint

# This will create schema in mySql database
# meaning it will create table:products 
# in database: TASK1
model.Base.metadata.create_all(bind=engine)
# this will start scrapping and return the categories_Dict as response
response = startWebScrapping()

# then to insert into products table
# i'm creating a list of rows
# [ {"product_name": Amplifiers, "category_name": 'Differential Amplifiers and ADC Drivers'},
#   "product_name": Amplifiers, "category_name": 'Instrumentation Amplifiers'},
#   ....
# ]
allProducts = []

for key,val in response.items():
    for subcategory in val:
        allProducts.append({"product_name": key, "category_name": subcategory})
print(len(allProducts))

# bult_insert_mappings will insert all rows in the table at the same time
db = SessionLocal()
db.bulk_insert_mappings(products, allProducts)
db.commit()


