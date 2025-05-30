from core.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Task(Base):
    title: Mapped[str] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(default=False)