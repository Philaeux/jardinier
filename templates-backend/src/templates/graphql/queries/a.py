from strawberry.types import Info

from templates.graphql.types.generic import ApiError, ApiSuccess


async def query_error_example(info: Info) -> ApiError:

    # Typical database access
    # with info.context['session_factory'](expire_on_commit=False) as session:
    # ...

    return ApiError(message="Not Implemented")


async def query_success_example(info: Info) -> ApiSuccess:

    # Typical database access
    # with info.context['session_factory'](expire_on_commit=False) as session:
    # ...

    return ApiSuccess(message="Nice")
