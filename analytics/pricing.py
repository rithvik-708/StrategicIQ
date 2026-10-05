def calculate_relative_pricing(brand_price: float, benchmark_price: float) -> float:
    """Calculates the relative price positioning matrix."""
    if benchmark_price <= 0:
        return 0.0
    return round(brand_price / benchmark_price, 4)
