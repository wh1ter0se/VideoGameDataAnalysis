def format_distance(distance: float | int, decimal_places: int = 3) -> str:
    if distance >= 1e9:
        return f"{round(distance / 1e9, decimal_places)} Gm"
    if distance >= 1e6:
        return f"{round(distance / 1e6, decimal_places)} Mm"
    if distance >= 1e3:
        return f"{round(distance / 1e3, decimal_places)} km"
    return f"{round(distance, decimal_places)} m"
