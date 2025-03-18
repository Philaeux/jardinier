import strawberry

from templates.graphql.mutations.a import mutation_error_example
from templates.graphql.queries.a import query_success_example, query_error_example
from templates.graphql.types.generated import strawberry_sqlalchemy_mapper


@strawberry.type
class Mutation:
    mutation_error_example = strawberry.mutation(resolver=mutation_error_example)


@strawberry.type
class Query:
    query_success_example = strawberry.field(resolver=query_success_example)
    query_error_example = strawberry.field(resolver=query_error_example)


strawberry_sqlalchemy_mapper.finalize()
additional_types = list(strawberry_sqlalchemy_mapper.mapped_types.values())
schema = strawberry.Schema(query=Query, mutation=Mutation, types=additional_types)
