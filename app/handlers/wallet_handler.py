from fastapi import APIRouter, Request, status
from fastapi_pagination import Page

from app.schemas.wallet_schema import WalletResponse, WalletCreate


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
) -> WalletResponse:
    """Get wallet data and save to DB."""
    async with request.app.state.db.get_master_session() as session:
        pass


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
    """Get wallet data and save to DB."""
    async with request.app.state.db.get_master_session() as session:
        pass
