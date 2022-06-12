from dataclasses import dataclass


@dataclass
class SourdoughBreadPlan:
    total_flour: int
    hydration: float
    sourdough: int
    sourdough_hydration: float
    salt: float
