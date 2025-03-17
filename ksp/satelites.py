import utils
from typing import List


class Antenna:

    model_name: str
    range: int

    def __init__(
        self,
        model_name: str,
        range: int,
    ) -> None:
        self.model_name = model_name
        self.range = range

    def get_label(self) -> str:
        return f"{self.model_name} ({utils.format_distance(self.range, 1)})"


# region Antennas


class RA2(Antenna):
    def __init__(self) -> None:
        self.model_name = "RA-2"
        self.range = int(200e6)


class RA15(Antenna):
    def __init__(self) -> None:
        self.model_name = "RA-15"
        self.range = int(10e9)


class RA100(Antenna):
    def __init__(self) -> None:
        self.model_name = "RA-100"
        self.range = int(100e9)


# endregion


class AntennaSet:

    set_name: str
    quantity: str
    antenna: Antenna

    def __init__(
        self,
        set_name: str,
        quantity: str,
        antenna: Antenna,
    ) -> None:
        self.set_name = set_name
        self.quantity = quantity
        self.antenna = antenna

    def get_label(self) -> str:
        return f"| <{self.set_name}> [{self.quantity}] {self.antenna.get_label()}"


class Vessel:
    name: str

    def __init__(
        self,
        name: str,
        antenna_sets: List[AntennaSet],
    ) -> None:
        self.name = name


class Constellation:

    name: str

    def __init__(
        self,
        constellation_name: str,
        orbital_height_m: str,
        orbital_body: str,
        vessel: Vessel,
    ):
        self.name = constellation_name

    def encode(self) -> str:
        pass
