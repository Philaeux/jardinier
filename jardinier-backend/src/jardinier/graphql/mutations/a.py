from strawberry.types import Info

from jardinier.graphql.types.generic import ApiError
from jardinier.utils.helpers import unpack_utilities


async def mutation_error_example(info: Info) -> ApiError:
    settings, session = unpack_utilities(info)

    return ApiError(message="Not Implemented")
