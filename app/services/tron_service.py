from tronpy import Tron


class TronService:
    @staticmethod
    async def get_wallet_data(address: str) -> dict:
        """Get wallet data from Tron."""
        client = Tron()
        account = client.get_account(address)
        return {
            "address": address,
            "trx_balance": account["balance"] / 1_000_000,
            "bandwidth": account.get("free_net_usage", 0),
            "energy": account.get("energy_usage", 0)
        }
