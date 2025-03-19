# How to add an orm mapping to strawberry type
from strawchemy import Strawchemy

from jardinier.database.measure import Measure

strawchemy = Strawchemy()

@strawchemy.type(Measure, include="all")
class MeasureGQL:
    pass
