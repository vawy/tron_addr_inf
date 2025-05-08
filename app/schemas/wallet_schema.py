from pydantic import BaseModel
from datetime import datetime


class WalletBase(BaseModel):
    address: str


class WalletCreate(WalletBase):
    trx_balance: float
    bandwidth: int
    energy: int
    is_success: bool
    error_message: str | None


class WalletResponse(WalletBase):
    trx_balance: float
    bandwidth: int
    bandwidth_limit: int
    energy: int
    energy_limit: int
    is_success: bool
    error_message: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
