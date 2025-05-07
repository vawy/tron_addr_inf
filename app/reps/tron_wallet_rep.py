from app.reps.base import BaseRep
from app.models import Wallet


class WalletRep(BaseRep):
    def __init__(self, session):
        super().__init__(session=session, model=Wallet)
