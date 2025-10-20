from typing import Iterable

def total_points(matches: Iterable[str]) -> int:
    """
    Повертає суму очок за списком рядків формату 'x:y'.
    x — голи нашої команди, y — суперника.
    Правила: перемога=3, нічия=1, поразка=0.
    """
    points = 0
    for m in matches:
        x_str, y_str = m.split(":")
        x, y = int(x_str), int(y_str)
        points += 3 if x > y else 1 if x == y else 0
    return points


