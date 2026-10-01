"""Temporary fixture used to validate AutoTest continuation ordering."""


def summarize(values: list[int]) -> dict[str, float]:
    """Return a few deterministic statistics for a non-empty list."""
    total = sum(values)
    return {
        "count": float(len(values)),
        "total": float(total),
        "average": total / len(values),
    }


def render_summary(values: list[int]) -> str:
    """Render the summary in a stable, human-readable form."""
    summary = summarize(values)
    return (
        f"count={summary['count']:.0f}, "
        f"total={summary['total']:.0f}, "
        f"average={summary['average']:.2f}"
    )
