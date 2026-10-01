"""Small fixture used to validate queued AutoTest session continuation."""


def summarize(values: list[int]) -> dict[str, float]:
    """Return basic statistics for a non-empty list of integers."""
    total = sum(values)
    return {
        "count": len(values),
        "sum": total,
        "average": total / len(values),
    }
