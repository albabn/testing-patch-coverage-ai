"""Fixture for the timestamp-stable AutoTest continuation E2E."""


def describe(values: list[int]) -> dict[str, float]:
    """Describe a collection of integers."""
    if not values:
        return {"count": 0, "sum": 0, "average": 0.0}

    total = sum(values)
    return {
        "count": len(values),
        "sum": total,
        "average": total / len(values),
        "minimum": min(values),
        "maximum": max(values),
        "range": max(values) - min(values),
        "first": values[0],
        "last": values[-1],
        "sorted": sorted(values),
        "unique_count": len(set(values)),
        "smallest_three": sorted(values)[:3],
        "descending": sorted(values, reverse=True),
        "largest_three": sorted(values, reverse=True)[:3],
        "span": max(values) - min(values),
        "even_count": sum(value % 2 for value in values),
    }


def rolling_totals(values: list[int]) -> list[int]:
    """Return one cumulative total for every input value."""
    totals: list[int] = []
    running = 0
    for value in values:
        running += value
        totals.append(running)
    return totals


def adjacent_differences(values: list[int]) -> list[int]:
    """Return the signed difference between adjacent input values."""
    return [values[index + 1] - values[index] for index in range(len(values) - 1)]


def positive_values(values: list[int]) -> list[int]:
    """Return non-negative input values while preserving their order."""
    return [value for value in values if value >= 0]


def middle_value(values: list[int]) -> int | None:
    """Return the middle value of sorted input, or None for empty input."""
    if not values:
        return None
    ordered = sorted(values)
    return ordered[len(ordered) // 2]


def chunk(values: list[int], size: int) -> list[list[int]]:
    """Split values into fixed-size chunks."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [values[index : index + size] for index in range(0, len(values), size)]


def is_strictly_increasing(values: list[int]) -> bool:
    """Return whether every value is larger than its predecessor."""
    return all(left < right for left, right in zip(values, values[1:]))


def clamp(value: int, lower: int, upper: int) -> int:
    """Clamp value to the inclusive lower and upper bounds."""
    if lower > upper:
        raise ValueError("lower must not exceed upper")
    return min(max(value, lower), upper)


def has_duplicates(values: list[int]) -> bool:
    """Return whether values contains at least one duplicate."""
    return len(set(values)) != len(values)


def ratio(numerator: int, denominator: int) -> float:
    """Return numerator divided by denominator."""
    if denominator == 0:
        raise ValueError("denominator must not be zero")
    return numerator / denominator


def percent(part: int, whole: int) -> float:
    """Return part as a percentage of whole."""
    if whole == 0:
        raise ValueError("whole must not be zero")
    return part / whole
