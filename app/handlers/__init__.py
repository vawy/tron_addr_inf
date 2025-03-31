from app.handlers.wallet_handler import router as wallet_router

routes = [
    wallet_router
]

__all__ = [
    "routes",
]
