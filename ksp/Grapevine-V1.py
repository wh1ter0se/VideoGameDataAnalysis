import enums
import numpy as np
import bodies
import graphviz as gv  # type: ignore
import satelites as sat
from typing import List

# region Dot Graph Setup
dot = gv.Digraph("Grapvevine-V1")

dot.attr(fontname="Helvetica,Arial,sans-serif")
dot.attr(overlap="false")
dot.attr(splines="true")
dot.attr("node", fontname="Helvetica,Arial,sans-serif")
dot.attr("edge", fontname="Helvetica,Arial,sans-serif")
dot.attr("graph", ranksep="3.0")
dot.attr(rankdir="LR")
dot.attr("node", fontsize="16", shape="record")

# endregion

# region Vessels
IvyPL1A = sat.Vessel(
    "Ivy PL1A",
    [
        sat.AntennaSet("outer_main", 3, sat.RA2()),
        sat.AntennaSet("outer_aux1", 3, sat.RA2()),
        sat.AntennaSet("scanner_network", 6, sat.RA2()),
        sat.AntennaSet("active_vessel", 1, sat.RA100()),
        sat.AntennaSet("loopback", 4, sat.RA2()),
    ],
)
IvyPL1B = sat.Vessel(
    "Ivy PL1B",
    [
        sat.AntennaSet("mission_control", 1, sat.RA2()),
        sat.AntennaSet("scanner_network", 6, sat.RA2()),
        sat.AntennaSet("outer_main", 3, sat.RA2()),
        sat.AntennaSet("outer_aux1", 3, sat.RA2()),
        sat.AntennaSet("outer_aux2", 3, sat.RA2()),
        sat.AntennaSet("active_vessel", 1, sat.RA100()),
        sat.AntennaSet("loopback", 4, sat.RA2()),
    ],
)
IvyPL1C = sat.Vessel(
    "Ivy PL1C",
    [
        sat.AntennaSet("outer_main", 3, sat.RA2()),
        sat.AntennaSet("outer_aux1", 3, sat.RA2()),
        sat.AntennaSet("outer_aux2", 3, sat.RA2()),
        sat.AntennaSet("outer_aux3", 3, sat.RA2()),
        sat.AntennaSet("outer_aux4", 3, sat.RA2()),
        sat.AntennaSet("outer_aux5", 3, sat.RA2()),
        sat.AntennaSet("scanner_network", 6, sat.RA2()),
        sat.AntennaSet("active_vessel", 1, sat.RA100()),
        sat.AntennaSet("loopback", 4, sat.RA2()),
    ],
)
IvyPH1 = sat.Vessel(
    "Ivy PH1",
    [
        sat.AntennaSet("outer", 3, sat.RA100()),
        sat.AntennaSet("inner", 3, sat.RA2()),
        sat.AntennaSet("planet_cone", 1, sat.RA2()),
        sat.AntennaSet("active_vessel", 1, sat.RA100()),
        sat.AntennaSet("loopback", 4, sat.RA2()),
    ],
)
IvyMPS1 = sat.Vessel(
    "Ivy MPS1",
    [
        sat.AntennaSet("outer", 3, sat.RA2()),
        sat.AntennaSet("planet_cone", 1, sat.RA2()),
        sat.AntennaSet("active_vessel", 1, sat.RA100()),
        sat.AntennaSet("loopback", 4, sat.RA2()),
    ],
)
IvyMH1 = sat.Vessel(
    "Ivy MH1",
    [
        sat.AntennaSet("outer", 3, sat.RA2()),
        sat.AntennaSet("scanner_network", 6, sat.RA2()),
        sat.AntennaSet("planet_cone", 1, sat.RA2()),
        sat.AntennaSet("active_vessel", 1, sat.RA100()),
        sat.AntennaSet("loopback", 4, sat.RA2()),
    ],
)
IvyST1 = sat.Vessel(
    "Ivy ST1",
    [
        sat.AntennaSet("mission_control", 1, sat.RA100()),
        sat.AntennaSet("inner", 3, sat.RA100()),
        sat.AntennaSet("outer", 3, sat.RA100()),
        sat.AntennaSet("planet_network", 3, sat.RA100()),
        sat.AntennaSet("active_vessel", 1, sat.RA100()),
        sat.AntennaSet("loopback", 3, sat.RA100()),
    ],
)

# endregion

# region Constellations
KSC = sat.Station(
    name="KSC",
    group=bodies.Kerbin,
    antenna=sat.TrackingStation(),
)
KerbinPL = sat.Constellation(
    name="Kerbin-PL",
    quantity=6,
    orbital_sma_m=80e6,
    orbital_body=bodies.Kerbin,
    group=bodies.Kerbin,
    vessel=IvyPL1B,
)
KerbinPH = sat.Constellation(
    name="Kerbin-PH",
    quantity=6,
    orbital_sma_m=80e6,
    orbital_body=bodies.Kerbin,
    group=bodies.Kerbin,
    vessel=IvyPH1,
)
KerbinPS = sat.Constellation(
    name="Kerbin-PS",
    quantity=12,
    orbital_sma_m=1.5e6,
    orbital_body=bodies.Kerbin,
    group=bodies.Kerbin,
    vessel=IvyMPS1,
)
MunMH = sat.Constellation(
    name="Mun-MH",
    quantity=6,
    orbital_sma_m=1.4e6,
    orbital_body=enums.Moon.Mun,
    group=bodies.Kerbin,
    vessel=IvyMH1,
)
MunMPS = sat.Constellation(
    name="Mun-MPS",
    quantity=12,
    orbital_sma_m=1.4e6,
    orbital_body=enums.Moon.Mun,
    group=bodies.Kerbin,
    vessel=IvyMPS1,
)
MinmusMH = sat.Constellation(
    name="Minmus-MH",
    quantity=6,
    orbital_sma_m=1.4e6,
    orbital_body=enums.Moon.Minmus,
    group=bodies.Kerbin,
    vessel=IvyMH1,
)
MinmusMPS = sat.Constellation(
    name="Minmus-MPS",
    quantity=12,
    orbital_sma_m=1.4e6,
    orbital_body=enums.Moon.Minmus,
    group=bodies.Kerbin,
    vessel=IvyMPS1,
)
DunaPL = sat.Constellation(
    name="Duna-PL",
    quantity=6,
    orbital_sma_m=80e6,
    orbital_body=bodies.Duna,
    group=bodies.Duna,
    vessel=IvyPL1A,
)
DunaPH = sat.Constellation(
    name="Duna-PH",
    quantity=6,
    orbital_sma_m=80e6,
    orbital_body=bodies.Duna,
    group=bodies.Duna,
    vessel=IvyPH1,
)
DunaPS = sat.Constellation(
    name="Duna-PS",
    quantity=12,
    orbital_sma_m=1.5e6,
    orbital_body=bodies.Duna,
    group=bodies.Duna,
    vessel=IvyMPS1,
)
IkeMH = sat.Constellation(
    name="Ike-MH",
    quantity=6,
    orbital_sma_m=1.4e6,
    orbital_body=enums.Moon.Ike,
    group=bodies.Duna,
    vessel=IvyMH1,
)
IkeMPS = sat.Constellation(
    name="Ike-MPS",
    quantity=12,
    orbital_sma_m=1.4e6,
    orbital_body=enums.Moon.Ike,
    group=bodies.Duna,
    vessel=IvyMPS1,
)
KerbolSTA = sat.Constellation(
    name="Kerbol-ST-A",
    quantity=6,
    orbital_sma_m=(5263138304 + 6315765981) / 2,
    orbital_body=bodies.Kerbol,
    group=bodies.Moho,
    vessel=IvyST1,
)
KerbolSTB = sat.Constellation(
    name="Kerbol-ST-B",
    quantity=6,
    orbital_sma_m=(9931011387 + 9734357701) / 2,
    orbital_body=bodies.Kerbol,
    group=bodies.Eve,
    vessel=IvyST1,
)
KerbolSTC = sat.Constellation(
    name="Kerbol-ST-C",
    quantity=6,
    orbital_sma_m=(13599840256 + 13599840256) / 2,
    orbital_body=bodies.Kerbol,
    group=bodies.Kerbin,
    vessel=IvyST1,
)
KerbolSTD = sat.Constellation(
    name="Kerbol-ST-D",
    quantity=6,
    orbital_sma_m=(20726155264 + 21783189163) / 2,
    orbital_body=bodies.Kerbol,
    group=bodies.Duna,
    vessel=IvyST1,
)
KerbolSTE = sat.Constellation(
    name="Kerbol-ST-E",
    quantity=6,
    orbital_sma_m=(40839348203 + 46761053692) / 2,
    orbital_body=bodies.Kerbol,
    group=bodies.Dres,
    vessel=IvyST1,
)
KerbolSTF = sat.Constellation(
    name="Kerbol-ST-F",
    quantity=6,
    orbital_sma_m=(40839348203 + 46761053692) / 2,
    orbital_body=bodies.Kerbol,
    group=bodies.Jool,
    vessel=IvyST1,
)
# endregion

# region Connections
connections: List[sat.Connection] = [
    *[  # Plantery Inter-layer,
        # Kerbin
        sat.RelayConnection(KerbinPH, "inner", KerbinPL, "outer_main"),
        sat.RelayConnection(KerbinPS, "outer", KerbinPL, "scanner_network"),
        sat.RelayConnection(MunMH, "outer", KerbinPL, "outer_aux1"),
        sat.RelayConnection(MunMPS, "outer", MunMH, "scanner_network"),
        sat.RelayConnection(MinmusMH, "outer", KerbinPL, "outer_aux2"),
        sat.RelayConnection(MinmusMPS, "outer", MinmusMH, "scanner_network"),
        # Duna
        sat.RelayConnection(DunaPL, "outer_main", DunaPH, "inner"),
        sat.RelayConnection(DunaPS, "outer", DunaPL, "scanner_network"),
        sat.RelayConnection(IkeMH, "outer", DunaPL, "outer_aux1"),
        sat.RelayConnection(IkeMPS, "outer", IkeMH, "scanner_network"),
    ],
    *[  # Kerbol Inter-layer
        sat.RelayConnection(KerbolSTA, "outer", KerbolSTB, "inner"),
        sat.RelayConnection(KerbolSTB, "outer", KerbolSTC, "inner"),
        sat.RelayConnection(KerbolSTD, "inner", KerbolSTC, "outer"),
        sat.RelayConnection(KerbolSTE, "inner", KerbolSTD, "outer"),
        sat.RelayConnection(KerbolSTF, "inner", KerbolSTE, "outer"),
    ],
    *[  # Planetary Networks
        sat.RelayConnection(KerbolSTC, "planet_network", KerbinPH, "outer"),
        sat.RelayConnection(DunaPH, "outer", KerbolSTD, "planet_network"),
    ],
]
relay_connections: List[sat.RelayConnection] = [
    _ for _ in connections if isinstance(_, sat.RelayConnection)
]
relay_constellations: List[sat.Constellation] = list(
    np.unique(
        [
            *[connection.constellation_from for connection in relay_connections],
            *[connection.constellation_to for connection in relay_connections],
        ]
    )
)
for constellation in relay_constellations:
    antenna_set_names = [antenna_set.name for antenna_set in constellation.vessel.antenna_sets]
    if "loopback" in antenna_set_names:
        connections.append(sat.Loopback(constellation=constellation))
    if "mission_control" in antenna_set_names:
        dot.node(
            name=KSC.name,
            label=KSC.get_label(),
            shape="record",
            group=KSC.group.name,
        )
        connections.append(
            sat.StationConnecion(
                constellation_from=constellation,
                station_to=KSC,
            )
        )
    if "planet_cone" in antenna_set_names:
        dot.node(
            name=constellation.orbital_body.name,
            label=constellation.orbital_body.name,
            shape="record",
            group=constellation.group.name,
        )
        connections.append(
            sat.BodyConnection(
                body_from=constellation.orbital_body,
                constellation_to=constellation,
            )
        )
    if "active_vessel" in antenna_set_names:
        dot.node(
            name=f"active_vessel_{constellation.group.name}",
            label=f"Active Vessel ({constellation.group.name})",
            shape="record",
            group=constellation.group.name,
        )
        connections.append(
            sat.VesselConnection(
                constellation=constellation,
            )
        )

# endregion

# region Planet Cones
# endregion

# region Build Graph
for constellation in relay_constellations:
    dot.node(
        name=constellation.name,
        label=constellation.get_label(),
        shape="record",
        group=constellation.group.name,
    )

for connection in connections:
    dot.edge(
        tail_name=connection.tail_name,
        head_name=connection.head_name,
        label=connection.label,
        concentrate="true",
    )
# endregion

dot.render("ksp/Grapevine-V1.dot")
