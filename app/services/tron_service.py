from tronpy import Tron
from tronpy.exceptions import ValidationError


class TronService:
    @staticmethod
    async def get_wallet_data(address: str) -> dict:
        """Get wallet data from Tron."""
        try:
            client = Tron()
            account = client.get_account(address)
            return {
                "address": address,
                "trx_balance": account["balance"] / 1_000_000,
                "bandwidth": account.get("free_net_usage", 0),
                "energy": account.get("energy_usage", 0),
                "is_success": True,
                "error_message": None
            }
        except ValidationError as e:
            return {
                "address": address,
                "trx_balance": 0,
                "bandwidth": 0,
                "energy": 0,
                "is_success": False,
                "error_message": str(e)
            }
