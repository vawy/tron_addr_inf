from app.reps.default_rep import DefaultRep
from app.models import TronWallet


class TronWalletRep(DefaultRep):
    def __init__(self, session):
        super().__init__(session=session, model=TronWallet)

    async def get_wallet(self, address: str):
        wallet_data = self.tron_service.get_wallet_data(address=address)
        result = self.create_one(body=wallet_data)
        return result
