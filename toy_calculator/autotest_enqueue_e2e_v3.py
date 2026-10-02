"""Fixture for the timestamp-stable AutoTest continuation E2E."""


def describe(values: list[int]) -> dict[str, float]:
    """Describe a non-empty collection of integers."""
    total = sum(values)
    return {
        "count": len(values),
        "sum": total,
        "average": total / len(values),
    }
