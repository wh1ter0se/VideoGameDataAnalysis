import utils
import enums
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


class TrackingStation(Antenna):
    def __init__(self) -> None:
        self.model_name = "Tracking Station"
        self.range = int(70e6)


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

    name: str
    quantity: int
    antenna: Antenna

    def __init__(
        self,
        name: str,
        quantity: int,
        antenna: Antenna,
    ) -> None:
        self.name = name
        self.quantity = quantity
        self.antenna = antenna

    def get_label(self) -> str:
        return f"\n| <{self.name}> [{self.quantity}] {self.antenna.get_label()}"


class Vessel:
    name: str
    antenna_sets: List[AntennaSet]

    def __init__(
        self,
        name: str,
        antenna_sets: List[AntennaSet],
    ) -> None:
        self.name = name
        self.antenna_sets = antenna_sets


class Constellation:

    name: str
    quantity: int
    orbital_sma_m: float
    orbital_body: enums.Star | enums.Planet | enums.Moon
    group: enums.Planet
    vessel: Vessel

    def __init__(
        self,
        name: str,
        quantity: int,
        orbital_sma_m: float,
        orbital_body: enums.Star | enums.Planet | enums.Moon,
        group: enums.Planet,
        vessel: Vessel,
    ):
        self.name = name
        self.quantity = quantity
        self.orbital_sma_m = orbital_sma_m
        self.orbital_body = orbital_body
        self.group = group
        self.vessel = vessel

    def get_label(self) -> str:
        label = (
            f"<f0>{self.name}\\n"
            + (f"({utils.format_distance(self.orbital_sma_m, 3)} \\| {self.orbital_body.name})\\n")
            + f"[{self.quantity}] {self.vessel.name} "
        )
        for antenna_set in self.vessel.antenna_sets:
            label += antenna_set.get_label()
        return label

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()


class Station(Constellation):

    antenna: Antenna

    def __init__(
        self,
        name: str,
        group: enums.Planet,
        antenna: Antenna,
    ):
        self.antenna = antenna
        super().__init__(
            name=name,
            quantity=1,
            orbital_sma_m=0,
            orbital_body=group,
            group=group,
            vessel=Vessel(name, [AntennaSet("station", 1, antenna)]),
        )

    def get_label(self) -> str:
        return f"{self.name}\\n {self.vessel.antenna_sets[0].get_label()}"


class Connection:

    tail_name: str
    head_name: str
    label: str

    def __init__(
        self,
        tail_name: str,
        head_name: str,
        label: str = "",
    ):
        self.tail_name = tail_name
        self.head_name = head_name
        self.label = label


class RelayConnection(Connection):
    def __init__(
        self,
        constellation_from: Constellation,
        antenna_set_from: str,
        constellation_to: Constellation,
        antenna_set_to: str,
    ) -> None:
        self.constellation_from = constellation_from
        self.antenna_set_from = antenna_set_from
        self.constellation_to = constellation_to
        self.antenna_set_to = antenna_set_to
        super().__init__(
            tail_name=f"{constellation_from.name}:{antenna_set_from}:e",
            head_name=f"{constellation_to.name}:{antenna_set_to}:w",
        )


class VesselConnection(Connection):
    def __init__(
        self,
        constellation: Constellation,
    ):
        super().__init__(
            tail_name=f"active_vessel_{constellation.group.name}:e",
            head_name=f"{constellation.name}:active_vessel:w",
        )


class BodyConnection(Connection):

    def __init__(
        self,
        body_from: enums.Star | enums.Planet | enums.Moon,
        constellation_to: Constellation,
    ) -> None:
        super().__init__(
            tail_name=f"{body_from.name}:e",
            head_name=f"{constellation_to.name}:planet_cone:w",
        )


class StationConnecion(Connection):
    def __init__(
        self,
        constellation_from: Constellation,
        station_to: Station,
    ) -> None:
        super().__init__(
            tail_name=f"{constellation_from.name}:mission_control:e",
            head_name=f"{station_to.name}:station:w",
        )


class Loopback(Connection):

    def __init__(self, constellation: Constellation):
        super().__init__(
            tail_name=f"{constellation.name}:loopback:w",
            head_name=f"{constellation.name}:loopback:w",
        )
