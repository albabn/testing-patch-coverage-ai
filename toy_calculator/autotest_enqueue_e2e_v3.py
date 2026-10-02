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
    return [values[index + 1] - values[index] for index in range(len(values))]
