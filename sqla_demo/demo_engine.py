

#machine_engine.py


from sqlalchemy import create_engine
from demo_config import DBASE_URI

engine = create_engine( DBASE_URI,
    client_encoding = 'utf8', # uses utf8
    echo=True) # prints postgres activity to stdout
