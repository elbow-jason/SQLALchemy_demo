


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Sample(Base):
    __tablename__ = 'samples'

    id              = Column(Integer, primary_key=True)
    lab_tech        = Column(String)
    receive_time    = Column(DateTime)

    def __repr__(self):
        return "<Sample(%r, %r)>" % (self.lab_tech, self.receive_time)


class Cell(Base):
    __tablename__ = 'cells'

    cell_id         = Column(Integer)