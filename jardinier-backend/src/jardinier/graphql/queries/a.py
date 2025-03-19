from strawberry.types import Info

from jardinier.graphql.types.generic import ApiError, ApiSuccess
from jardinier.utils.helpers import unpack_utilities


async def query_error_example(info: Info) -> ApiError:
    settings, session = unpack_utilities(info)

    return ApiError(message="Not Implemented")


async def query_success_example(info: Info) -> ApiSuccess:
    settings, session = unpack_utilities(info)

    return ApiSuccess(message="Nice")
