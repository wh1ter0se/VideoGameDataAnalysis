from enum import Enum


class Star(Enum):
    Kerbol = 0  # Sun


class Planet(Enum):
    Moho = 1  # Mercury
    Eve = 2  # Venus
    Kerbin = 3  # Earth
    Duna = 4  # Mars
    Dres = 5  # Ceres
    Jool = 6  # Jupiter
    Eeloo = 7  # Pluto


class Moon(Enum):
    Gilly = 201
    Mun = 301
    Minmus = 302
    Ike = 401
    Laythe = 601
    Vall = 602
    Tylo = 603
    Bop = 604
    Pol = 605
