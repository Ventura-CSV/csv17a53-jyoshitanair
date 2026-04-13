from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===
    seen = {}
    for k, v in mapping.items():
        if v in seen:
            # okay we've seen you before
            return (seen[k], v)
        seen[v] = k
    # injective!
    return None
    # === END TODO ===


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===
    unique_y = set(mapping.values())
    for t in target:
        if t not in unique_y:
            return t
    return None
    # === END TODO ===


def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    if x>=0:
        return int(x)
    elif x == int(x):
        return x
    else:
        return int(x) - 1
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    if x>=0:
        return int(x) + 1
    elif x = int(x):
        return x
    else:
        return int(x)
    # === END TODO ===
