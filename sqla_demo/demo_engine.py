

#machine_engine.py


from sqlalchemy import create_engine
from machine_config import DATABASE_URI

engine = create_engine( DATABASE_URI,
    client_encoding = 'utf8', # uses utf8
    echo=True) # prints postgres activity to stdout
