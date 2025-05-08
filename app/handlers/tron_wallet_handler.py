from fastapi import APIRouter, Request, status
from fastapi_pagination import Page

from app.schemas.wallet_schema import WalletResponse, WalletCreate
from app.reps.tron_wallet_rep import TronWalletRep


router = APIRouter(
    tags=["tron_wallet"],
    prefix="/tron_wallet"
)


@router.post(
    "/wallet_by_address/",
    status_code=status.HTTP_200_OK,
    summary="Get wallet info by address",
    description="Get wallet info by address",
    response_model=WalletResponse
)
async def get_wallet_info(
        request: Request,
        body: WalletCreate
):
    async with request.app.state.db.get_master_session() as session:
        tron_wallet_rep = TronWalletRep(session=session)
        return await tron_wallet_rep.get_wallet(address=body.address)


@router.get(
    "/wallets/",
    status_code=status.HTTP_200_OK,
    summary="Get wallets from db",
    description="Get wallets from db",
    response_model=Page[WalletResponse]
)
async def get_wallet_info(
        request: Request
) -> Page[WalletResponse]:
    async with request.app.state.db.get_master_session() as session:
        wallet_rep = TronWalletRep(session=session)
        return await wallet_rep.find_all()
