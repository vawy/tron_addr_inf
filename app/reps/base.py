from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.strategy_options import LoaderOption
from sqlalchemy.sql.selectable import Select

from starlette import status

from metadata import Base


class BaseRep:
    def __init__(
            self,
            session: AsyncSession,
            model: Base,
            options: list[LoaderOption] | None = None,
    ):
        self.session = session
        self.model = model

    def _build_default_query(self) -> Select:
        return select(self.model)

    async def find_all(self, query=None):
        if query is None:
            query = self._build_default_query()

        result = await self.session.scalars(query)
        result = result.all()
        return result

    async def create_one(self, model: Base, body: dict):
        for key, value in body.items():
            try:
                setattr(self.model, key, value)
            except AttributeError:
                pass
                # logging.warning(
                #     f"Can't assing attribute key: {key} with value: {value} to model {model.__table__}. You probably assigning value to hybrid_property")

        return model
