

#machine_app.py

#import al
from machine_engine import engine
from machine_session import session

import cell_tables
from cell_tables import Cell
from sqlalchemy import select

#import time for use of current datetime
import datetime




#Drop the cell table?

#generate a table
cell_tables.Base.metadata.create_all(engine)






session.add(current_cell)
session.commit()

query = session.query(Cell).filter_by(lab_tech='Jason Louis')
print query.all()


lab_tech_query = select_lab_tech('Jason Louis')