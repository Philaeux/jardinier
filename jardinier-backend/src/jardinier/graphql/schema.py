import strawberry

from jardinier.graphql.mutations.a import mutation_error_example
from jardinier.graphql.queries.measure import query_success_example, query_error_example


@strawberry.type
class Mutation:
    mutation_error_example = strawberry.mutation(resolver=mutation_error_example)


@strawberry.type
class Query:
    query_success_example = strawberry.field(resolver=query_success_example)
    query_error_example = strawberry.field(resolver=query_error_example)


schema = strawberry.Schema(query=Query, mutation=Mutation)
