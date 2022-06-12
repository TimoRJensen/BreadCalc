from dataclasses import dataclass

from BreadCalc.plans import SourdoughBreadPlan


@dataclass
class SourdoughBreadRecipe:
    flour_rest: float
    water_rest: float
    salt: float
    plan: SourdoughBreadPlan

    @property
    def sour_ratio(self) -> float:
        return 1 - (self.flour_rest / self.plan.total_flour)
