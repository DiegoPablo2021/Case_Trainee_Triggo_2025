import pytest
from src.marketing_strategies import MarketingStrategist

def test_suggest_strategies():
    strategist = MarketingStrategist()
    cluster_results = {
        0: {"average_spending": 1200, "loyalty": 0.9, "frequency": 4},
        1: {"average_spending": 600, "loyalty": 0.5, "frequency": 3},
        2: {"average_spending": 300, "loyalty": 0.2, "frequency": 1},
        3: {"average_spending": 400, "loyalty": 0.3, "frequency": 3}, # Edge case
    }
    
    strategies = strategist.suggest_strategies(cluster_results)
    
    assert len(strategies) == 4
    assert strategies[0] == "Target with exclusive offers and loyalty programs."
    assert strategies[1] == "Promote upselling and cross-selling opportunities."
    assert strategies[2] == "Encourage repeat purchases through discounts and promotions."
    assert strategies[3] == "Engage with personalized marketing campaigns to increase loyalty."

def test_suggest_strategies_empty():
    strategist = MarketingStrategist()
    strategies = strategist.suggest_strategies({})
    assert len(strategies) == 0
