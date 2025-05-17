def suggest_strategies(cluster_analysis_results):
    strategies = {}
    
    for cluster_id, analysis in cluster_analysis_results.items():
        if analysis['average_spending'] > 1000 and analysis['loyalty'] > 0.8:
            strategies[cluster_id] = "Target with exclusive offers and loyalty programs."
        elif analysis['average_spending'] > 500:
            strategies[cluster_id] = "Promote upselling and cross-selling opportunities."
        elif analysis['average_spending'] <= 500 and analysis['frequency'] < 2:
            strategies[cluster_id] = "Encourage repeat purchases through discounts and promotions."
        else:
            strategies[cluster_id] = "Engage with personalized marketing campaigns to increase loyalty."
    
    return strategies