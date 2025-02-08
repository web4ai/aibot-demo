from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/dbname"

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)

def get_database_session():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def get_order_data(order_id):
    session = get_database_session()
    order = session.query(Order).filter(Order.id == order_id).first()
    session.close()
    return order

def insert_order_data(product_name, quantity, price):
    session = get_database_session()
    new_order = Order(product_name=product_name, quantity=quantity, price=price)
    session.add(new_order)
    session.commit()
    session.close()