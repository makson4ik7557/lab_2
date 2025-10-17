class PortfolioHolder:
    DIVERSIFICATION_HIGH_RISK_THRESHOLD = 5
    DIVERSIFICATION_MODERATE_RISK_THRESHOLD = 15

    def __init__(self, risk_appetite: str = "Moderate"):
        self.risk_appetite = risk_appetite

    def calculate_risk_level(self, diversification_score: int) -> str:
        if diversification_score > PortfolioHolder.DIVERSIFICATION_MODERATE_RISK_THRESHOLD:
            risk = "Low"
        elif diversification_score > PortfolioHolder.DIVERSIFICATION_HIGH_RISK_THRESHOLD:
            risk = "Moderate"
        else:
            risk = "High"
        return f"[PORTFOLIO] Загальний ризик: {risk} (Апетит: {self.risk_appetite})"
