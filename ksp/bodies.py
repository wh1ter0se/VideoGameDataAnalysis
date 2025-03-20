from __future__ import annotations

from typing import List


class Body:

    name: str

    # Physical
    radius_m: float
    mass_kg: float

    # Orbital
    semi_major_axis_m: float  # SMA
    apoapsis_m: float
    periapsis_m: float
    eccentricity: float
    inclination_deg: float
    argument_of_periapsis_deg: float
    mean_anomaly_rad: float  # MNA

    # Relationships
    parent: Body | None
    children: List[Body] | List[None] | None

    def __init__(
        self,
        name: str,
        radius_m: float,
        mass_kg: float,
        apoapsis_m: float,
        periapsis_m: float,
        inclination_deg: float,
        argument_of_periapsis_deg: float,
        mean_anomaly_rad: float,
        parent: Body | None,
    ):
        self.name = name
        self.radius_m = radius_m
        self.mass_kg = mass_kg
        self.apoapsis_m = apoapsis_m
        self.periapsis_m = periapsis_m
        self.inclination_deg = inclination_deg
        self.argument_of_periapsis_deg = argument_of_periapsis_deg
        self.mean_anomaly_rad = mean_anomaly_rad
        self.parent = parent

        self.semi_major_axis_m = (self.apoapsis_m + self.periapsis_m) / 2
        self.eccentricity = (self.apoapsis_m - self.periapsis_m) / self.semi_major_axis_m


# region Star
Kerbol = Body(
    name="Kerbol",
    radius_m=261600000,
    mass_kg=int(1.7565459e28),
    apoapsis_m=1.0,
    periapsis_m=1.0,
    inclination_deg=0,
    argument_of_periapsis_deg=0,
    mean_anomaly_rad=0,
    parent=None,
)
# endregion

# region Planet
Moho = Body(
    name="Moho",
    radius_m=250000,
    mass_kg=int(2.5263314e21),
    apoapsis_m=6315765981,
    periapsis_m=4210510628,
    inclination_deg=7.0,
    argument_of_periapsis_deg=15.0,
    mean_anomaly_rad=3.14,
    parent=Kerbol,
)
Eve = Body(
    name="Eve",
    radius_m=700000,
    mass_kg=int(1.2243980e23),
    apoapsis_m=9931011387,
    periapsis_m=9734357701,
    inclination_deg=2.1,
    argument_of_periapsis_deg=0.0,
    mean_anomaly_rad=3.14,
    parent=Kerbol,
)
Kerbin = Body(
    name="Kerbin",
    radius_m=600000,
    mass_kg=int(5.2915158e22),
    apoapsis_m=13599840256,
    periapsis_m=13599840256,
    inclination_deg=0.0,
    argument_of_periapsis_deg=0.0,
    mean_anomaly_rad=3.14,
    parent=Kerbol,
)
Duna = Body(
    name="Duna",
    radius_m=320000,
    mass_kg=int(4.5154270e21),
    apoapsis_m=21783189163,
    periapsis_m=19669121365,
    inclination_deg=0.06,
    argument_of_periapsis_deg=0.0,
    mean_anomaly_rad=3.14,
    parent=Kerbol,
)
Dres = Body(
    name="Dres",
    radius_m=138000,
    mass_kg=int(3.2190937e20),
    apoapsis_m=46761053692,
    periapsis_m=34917642714,
    inclination_deg=5.0,
    argument_of_periapsis_deg=90.0,
    mean_anomaly_rad=3.14,
    parent=Kerbol,
)
Jool = Body(
    name="Jool",
    radius_m=6000000,
    mass_kg=int(4.2332127e24),
    apoapsis_m=72212238387,
    periapsis_m=65334882253,
    inclination_deg=1.304,
    argument_of_periapsis_deg=0.0,
    mean_anomaly_rad=0.1,
    parent=Kerbol,
)
Eeloo = Body(
    name="Eeloo",
    radius_m=210000,
    mass_kg=int(1.1149224e21),
    apoapsis_m=113549713200,
    periapsis_m=66687926800,
    inclination_deg=6.15,
    argument_of_periapsis_deg=260.0,
    mean_anomaly_rad=3.14,
    parent=Kerbol,
)
# endregion

# region Bodys
Gilly = Body(
    name="Gilly",
    radius_m=13000,
    mass_kg=int(1.2420363e17),
    apoapsis_m=48825000,
    periapsis_m=14175000,
    inclination_deg=12.0,
    argument_of_periapsis_deg=10.0,
    mean_anomaly_rad=0.9,
    parent=Moho,
)
Mun = Body(
    name="Mun",
    radius_m=200000,
    mass_kg=int(9.7599066e20),
    apoapsis_m=12000000,
    periapsis_m=12000000,
    inclination_deg=0.0,
    argument_of_periapsis_deg=0.0,
    mean_anomaly_rad=1.7,
    parent=Kerbin,
)
Minmus = Body(
    name="Minmus",
    radius_m=60000,
    mass_kg=int(2.6457580e19),
    apoapsis_m=47000000,
    periapsis_m=47000000,
    inclination_deg=6.0,
    argument_of_periapsis_deg=38.0,
    mean_anomaly_rad=0.9,
    parent=Kerbin,
)
Ike = Body(
    name="Ike",
    radius_m=130000,
    mass_kg=int(2.7821615e20),
    apoapsis_m=3296000,
    periapsis_m=3104000,
    inclination_deg=0.2,
    argument_of_periapsis_deg=0.0,
    mean_anomaly_rad=1.7,
    parent=Duna,
)
# Laythe = Body(
#     name="Laythe",
#     radius_m=None,
#     mass_kg=None,
#     apoapsis_m=None,
#     periapsis_m=None,
#     inclination_deg=None,
#     argument_of_periapsis_deg=None,
#     mean_anomaly_rad=None,
#     parent=None,
# )
# Vall = Body(
#     name="Vall",
#     radius_m=None,
#     mass_kg=None,
#     apoapsis_m=None,
#     periapsis_m=None,
#     inclination_deg=None,
#     argument_of_periapsis_deg=None,
#     mean_anomaly_rad=None,
#     parent=None,
# )
# Tylo = Body(
#     name="Tylo",
#     radius_m=None,
#     mass_kg=None,
#     apoapsis_m=None,
#     periapsis_m=None,
#     inclination_deg=None,
#     argument_of_periapsis_deg=None,
#     mean_anomaly_rad=None,
#     parent=None,
# )
# Bop = Body(
#     name="Bop",
#     radius_m=None,
#     mass_kg=None,
#     apoapsis_m=None,
#     periapsis_m=None,
#     inclination_deg=None,
#     argument_of_periapsis_deg=None,
#     mean_anomaly_rad=None,
#     parent=None,
# )
# Pol = Body(
#     name="Pol",
#     radius_m=None,
#     mass_kg=None,
#     apoapsis_m=None,
#     periapsis_m=None,
#     inclination_deg=None,
#     argument_of_periapsis_deg=None,
#     mean_anomaly_rad=None,
#     parent=None,
# )
# endregion
