"""Small fixture used to validate queued AutoTest session continuation."""


def summarize(values: list[int]) -> dict[str, float]:
    """Return basic statistics for a list of integers."""
    if not values:
        return {"count": 0, "sum": 0, "average": 0.0}

    total = sum(values)
    return {
        "count": len(values),
        "sum": total,
        "average": total / len(values),
    }
