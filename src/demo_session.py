
from sqlalchemy.orm import sessionmaker
from machine_engine import engine

#use Session class constructor sessionmaker
Session = sessionmaker(bind=engine)

#create new session from Session class
session = Session()
