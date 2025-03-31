from sqlalchemy import Column, String, Numeric, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

from app.utils.mixins import IdMixin, TimestampMixin

Base = declarative_base()

class Wallet(IdMixin, TimestampMixin, Base):
    """Tron wallet information."""
    __tablename__ = "wallets"

    address = Column(String(34), nullable=False, index=True)
    trx_balance = Column(Numeric(20, 6), default=0.0)
    bandwidth = Column(Integer, default=0)
    bandwidth_limit = Column(Integer, default=0)
    energy = Column(Integer, default=0)
    energy_limit = Column(Integer, default=0)
    is_success = Column(Boolean, default=True)
    error_message = Column(String, nullable=True)
