import pandas as pd
import numpy as np
from typing import Dict

def calculate_market_sizing(population: int, penetration_rate: float, avg_revenue_per_user: float, sam_filter: float, som_filter: float) -> Dict[str, float]:
    """Calculates TAM, SAM, and SOM deterministically."""
    tam = population * penetration_rate * avg_revenue_per_user
    sam = tam * sam_filter
    som = sam * som_filter
    
    return {
        "TAM": round(tam, 2),
        "SAM": round(sam, 2),
        "SOM": round(som, 2)
    }

def calculate_cagr(beginning_value: float, ending_value: float, years: int) -> float:
    """Calculates Compound Annual Growth Rate."""
    if beginning_value <= 0 or years <= 0:
        return 0.0
    return round(((ending_value / beginning_value) ** (1 / years)) - 1, 4)
