from database import Base
from sqlalchemy import Column, Integer, String, UniqueConstraint


class Notice(Base):
    __tablename__ = 'notice'
    __table_args__ = (UniqueConstraint('univ', 'title', name='univ_noctice'), )
    id = Column(Integer, primary_key=True)
    univ = Column(String, nullable=False)
    title = Column(String, nullable=False)
    link = Column(String, nullable=True)
