class PortfolioHolder:
    def __init__(self, risk_appetite: str = "Moderate"):
        self.risk_appetite = risk_appetite

    def calculate_risk_level(self, diversification_score: int) -> str:
        if diversification_score > 15:
            risk = "Low"
        elif diversification_score > 5:
            risk = "Moderate"
        else:
            risk = "High"
        return f"[PORTFOLIO] Загальний ризик: {risk} (Апетит: {self.risk_appetite})"