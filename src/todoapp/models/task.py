from sqlalchemy import Boolean, Column, Integer, String

from todoapp.config.database import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String(10), unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
