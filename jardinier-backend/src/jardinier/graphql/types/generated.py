from strawchemy import Strawchemy, StrawchemyConfig
from jardinier.database.measure import Measure

strawchemy = Strawchemy("sqlite")

@strawchemy.type(Measure, include="all")
class MeasureGQL:
    pass

@strawchemy.filter(Measure, include="all")
class MeasureFilter:
    pass

@strawchemy.order(Measure, include="all")
class MeasureOrderBy:
    pass
