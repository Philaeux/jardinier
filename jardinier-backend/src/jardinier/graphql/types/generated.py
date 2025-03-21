from strawchemy import Strawchemy

from jardinier.database.measure import Measure

strawchemy = Strawchemy()


@strawchemy.type(Measure, include="all")
class MeasureGQL:
    pass

@strawchemy.filter_input(Measure, include="all")
class MeasureFilter:
    pass

@strawchemy.order_by_input(Measure, include="all")
class MeasureOrderBy:
    pass
