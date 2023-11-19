from sqlalchemy import Column, String, Integer, Boolean

from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id_ = Column(Integer, primary_key=True)
    content = Column(String)
    is_done = Column(Boolean, default=False)
    number = Column(Integer)

    def __repr__(self):
        return f'Task(id_={self.id_}, content={self.content}, is_done={self.is_done}, number={self.number}'
