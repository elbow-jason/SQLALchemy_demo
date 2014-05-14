#populate_cell.py

import cell_tables
from cell_tables import Cell
import datetime


current_cells = [
        Cell(receive_time=datetime.datetime.now(), lab_tech="Jason Louis"),
        Cell(receive_time=datetime.datetime.now(), lab_tech="Jack Bean"),
        Cell(receive_time=datetime.datetime.now(), lab_tech="Nota Reelprsn"),
        Cell(receive_time=datetime.datetime.now(), lab_tech="Michael Meyer"),
        Cell(receive_time=datetime.datetime.now(), lab_tech="Dan Huber")
        ]



