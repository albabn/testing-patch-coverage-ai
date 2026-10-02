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
    }
