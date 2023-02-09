from sqlalchemy.schema import Column, ForeignKey
from datetime import datetime
from sqlalchemy import Column, Integer, String, Date, JSON, ForeignKey, Date
from sqlalchemy.types import String, Integer, Text
from sqlalchemy.orm import relationship
from database import Base

# products class defines a table named "products" in the database with the tablename property.
class products(Base):
    __tablename__ = "products"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    product_category = Column(String(100))
    subCategory_name = Column(String(100))
    product_name = Column(String(100))
    description = Column(Text)



    