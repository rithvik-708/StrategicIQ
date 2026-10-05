import pandas as pd

def calculate_qcommerce_unit_economics(aov: float, cogs_pct: float, delivery_cost: float, dark_store_ops: float) -> pd.DataFrame:
    """Calculates Contribution Margin per order for Quick-Commerce."""
    gross_margin = aov * (1 - cogs_pct)
    contribution_margin = gross_margin - delivery_cost - dark_store_ops
    cm_margin_pct = contribution_margin / aov
    
    return pd.DataFrame([{
        "AOV": aov,
        "Gross Margin": gross_margin,
        "Delivery Cost": delivery_cost,
        "Dark Store Ops": dark_store_ops,
        "Contribution Margin": contribution_margin,
        "CM %": cm_margin_pct
    }])
