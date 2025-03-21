import strawberry

from jardinier.graphql.types.generated import strawchemy, MeasureFilter, MeasureOrderBy, MeasureGQL


@strawberry.type
class Query:
    measures: list[MeasureGQL] = strawchemy.field(filter_input=MeasureFilter, order_by=MeasureOrderBy, pagination=True)


schema = strawberry.Schema(query=Query)
