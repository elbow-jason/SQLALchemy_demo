#select_all_cells.py

from sqlalchemy import select
from machine_session import session

def select_labtech(lab_person):
    sel = select([Cell.lab_tech, Cell.receive_time]).\
        where(Cell.labtech == lab_person).\
        order_by(Cell.id)

    session.connection().execute(sel).fetchall()
