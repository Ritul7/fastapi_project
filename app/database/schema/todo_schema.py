from sqlalchemy import Column, Integer, String, Boolean, VARCHAR, DateTime
from datetime import timezone, datetime

from ..db import Base

class TodoSchema(Base):             # Base tells SQLAlchemy, this class represents a database table

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))