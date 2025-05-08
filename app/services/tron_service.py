from tronpy import Tron
from tronpy.exceptions import ValidationError

from app.schemas.wallet_schema import WalletCreate


class TronService:
    @staticmethod
    async def get_wallet_data(address: str) -> WalletCreate:
        """Get wallet data from Tron."""
        try:
            client = Tron()
            account = client.get_account(address)
            return WalletCreate(
                address=address,
                trx_balance=account['balance'] / 100_000_000,
                bandwidth=account.get('free_net_usage', 0),
                energy=account.get("energy_usage", 0),
                is_success=True,
                error_message=None
            )
        except ValidationError as e:
            return WalletCreate(
                address=address,
                trx_balance=0,
                bandwidth=0,
                energy=0,
                is_success=False,
                error_message=str(e)
            )
