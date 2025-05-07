from sqlalchemy import Column, String, Numeric, Integer, Boolean

from metadata import Base

from app.utils.mixins import IdMixin, TimestampMixin


class TronWallet(IdMixin, TimestampMixin, Base):
    __tablename__ = "tron_wallet"

    address = Column(String(34), nullable=False, index=True)
    trx_balance = Column(Numeric(20, 6), default=0.0)
    bandwidth = Column(Integer, default=0)
    bandwidth_limit = Column(Integer, default=0)
    energy = Column(Integer, default=0)
    energy_limit = Column(Integer, default=0)
    is_success = Column(Boolean, default=True)
    error_message = Column(String, nullable=True)
