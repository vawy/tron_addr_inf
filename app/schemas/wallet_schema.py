from pydantic import BaseModel
from datetime import datetime


class WalletBase(BaseModel):
    address: str


class WalletCreate(WalletBase):
    pass


class WalletResponse(WalletBase):
    trx_balance: float
    bandwidth: int
    bandwidth_limit: int
    energy: int
    energy_limit: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
