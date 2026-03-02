from typing import Dict, Any
from src.logger import get_logger

logger = get_logger(__name__)


class MarketingStrategist:
    """
    A class to suggest and manage marketing strategies based on cluster attributes.
    """
    def __init__(self):
        # We can eventually load rules from a DB or configuration file
        pass

    def suggest_strategies(self, cluster_analysis_results: Dict[int, Dict[str, Any]]) -> Dict[int, str]:
        """
        Suggest marketing strategies based on cluster characteristics.
        """
        if not cluster_analysis_results:
            logger.warning("No cluster analysis results provided to suggest_strategies.")
            return {}
            
        logger.info(f"Generating strategies for {len(cluster_analysis_results)} clusters...")
        strategies = {}

        for cluster_id, analysis in cluster_analysis_results.items():
            avg_spending = analysis.get("average_spending", 0)
            loyalty = analysis.get("loyalty", 0)
            freq = analysis.get("frequency", 0)
            
            if avg_spending > 1000 and loyalty > 0.8:
                strategies[cluster_id] = "Target with exclusive offers and loyalty programs."
            elif avg_spending > 500:
                strategies[cluster_id] = "Promote upselling and cross-selling opportunities."
            elif avg_spending <= 500 and freq < 2:
                strategies[cluster_id] = "Encourage repeat purchases through discounts and promotions."
            else:
                strategies[cluster_id] = "Engage with personalized marketing campaigns to increase loyalty."
                
            logger.debug(f"Assigned strategy to Cluster {cluster_id}: {strategies[cluster_id]}")

        logger.info("Marketing strategies formulated.")
        return strategies

# Backward compatibility implementation
_strategist = MarketingStrategist()

def suggest_strategies(cluster_analysis_results: Dict[int, Dict[str, Any]]) -> Dict[int, str]:
    return _strategist.suggest_strategies(cluster_analysis_results)