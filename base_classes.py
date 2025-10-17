import random

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


class Stock:
    TOTAL_ASSETS_TRACKED = 0

    def __init__(self, ticker: str, name: str, initial_price: float, sector: str):
        self.ticker = ticker
        self.name = name
        self._sector = sector
        self.__current_price = self._validate_price(initial_price)
        self.__shares_outstanding = random.randint(100_000_000, 1_000_000_000)
        Stock.TOTAL_ASSETS_TRACKED += 1

    @property
    def current_price(self) -> float:
        return self.__current_price

    @current_price.setter
    def current_price(self, new_price: float):
        if new_price <= 0:
            print(f"[ERROR] Ціна {self.ticker} не може бути нульовою або негативною. Зміна відхилена.")
            return
        self.__current_price = new_price
        print(f"-> Ціна {self.ticker} оновлена до ${self.__current_price:.2f}.")

    def _validate_price(self, price: float) -> float:
        return price if price > 0 else 10.0

    def get_summary(self) -> str:
        return (f"[STOCK] {self.ticker} ({self.name}), Ціна: ${self.current_price:.2f}, "
                f"Сектор: {self._sector}")

    def pay_dividend(self, amount: float):
        print(f"*** {self.name} виплачує дивіденди: ${amount:.2f} ***")
        self.current_price -= amount * 0.85

    @staticmethod
    def get_exchange_name() -> str:
        return "NYSE/NASDAQ"

    def get_shares_count(self) -> int:
        return self.__shares_outstanding