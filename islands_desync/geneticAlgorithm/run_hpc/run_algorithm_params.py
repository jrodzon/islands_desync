import dataclasses


@dataclasses.dataclass(kw_only=True)
class RunAlgorithmParams:
    island_count: int
    number_of_emigrants: int
    migration_interval: int
    dda: str
    tta: str
    series_number: int
