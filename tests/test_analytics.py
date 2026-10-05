import pytest
import plotly.express as px
from analytics.sizing import calculate_market_sizing
from analytics.unit_economics import calculate_qcommerce_unit_economics

def test_market_sizing():
    # Example: 100M population, 10% penetration, $50 ARPU
    result = calculate_market_sizing(100_000_000, 0.10, 50.0, 0.40, 0.15)
    
    assert result["TAM"] == 500_000_000.0  # $500M
    assert result["SAM"] == 200_000_000.0  # $200M (40% of TAM)
    assert result["SOM"] == 30_000_000.0   # $30M (15% of SAM)

def test_plotly_json_export():
    df = calculate_qcommerce_unit_economics(aov=450, cogs_pct=0.75, delivery_cost=45, dark_store_ops=30)
    
    # Verify math
    assert df.iloc[0]["Contribution Margin"] == 37.5  # 450 - 337.5 - 45 - 30
    
    # Verify visualization export capability
    fig = px.bar(df, y=["Gross Margin", "Delivery Cost", "Dark Store Ops", "Contribution Margin"], title="Unit Economics Breakdown")
    json_data = fig.to_json()
    
    assert "data" in json_data
    assert "layout" in json_data
