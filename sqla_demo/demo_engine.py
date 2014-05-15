#machine_engine.py

from sqlalchemy import create_engine

def new_engine(uri):
    engine = create_engine(uri,
        client_encoding = 'utf8', # uses utf8
        echo=True) # prints postgres activity to stdout
    return engine