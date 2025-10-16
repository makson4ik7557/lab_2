from datetime import datetime
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


class TechStock(Stock):
    def __init__(self, ticker: str, name: str, initial_price: float, pe_ratio: float):
        super().__init__(ticker, name, initial_price, "Technology")
        self.pe_ratio = pe_ratio # sp

    def get_summary(self) -> str:
        base_info = super().get_summary()
        return f"{base_info} | Коефіцієнт P/E: {self.pe_ratio:.1f}"

    def forecast_growth(self, years: int): #sp
        growth = (30 / self.pe_ratio) * 10
        print(f"-> Прогноз росту {self.ticker} на {years} років: {growth:.2f}%")


class EtfFund(Stock, PortfolioHolder):
    def __init__(self, ticker: str, name: str, initial_price: float, asset_count: int):
        Stock.__init__(self, ticker, name, initial_price, "Fund")
        PortfolioHolder.__init__(self)
        self.asset_count = asset_count #sp

    def get_summary(self) -> str:
        base_info = Stock.get_summary(self)
        return f"[ETF] {base_info} | Активів у кошику: {self.asset_count}"

    def execute_trade(self, order_type: str, quantity: int):
        if order_type.upper() in ["BUY", "SELL"]:
            action = "КУПЛЕНО" if order_type.upper() == "BUY" else "ПРОДАНО"
            total_cost = quantity * self.current_price
            print(f"*** Виконано: {action} {quantity} лотів {self.ticker}. Сума: ${total_cost:.2f} ***")
        else:
            print("[ERROR] Невірний тип ордера. Використовуйте BUY або SELL.")


if __name__ == "__main__":
    msft = Stock("MSFT", "Microsoft Corp", 420.00, "Technology")
    jnj = Stock("JNJ", "Johnson & Johnson", 155.50, "Healthcare")
    aapl = TechStock("AAPL", "Apple Inc.", 175.00, 35.5)
    spy = EtfFund("SPY", "S&P 500 ETF", 520.00, 500)

    print("=" * 60)
    print(f"*** РИНОК: {Stock.get_exchange_name()} | Всього активів: {Stock.TOTAL_ASSETS_TRACKED} ***")
    print("=" * 60)

    print(f"Початкова ціна {aapl.ticker}: ${aapl.current_price:.2f}")

    aapl.current_price = 180.50
    aapl.current_price = 0
    print(f"Поточна ціна {aapl.ticker} після помилки: ${aapl.current_price:.2f}")
    print(f"Акцій JNJ в обігу: {jnj.get_shares_count():,}")

    print("-" * 60)

    msft.pay_dividend(0.75)
    aapl.forecast_growth(5)

    print("-" * 60)

    print(spy.calculate_risk_level(spy.asset_count))
    spy.execute_trade("BUY", 10)

    print("-" * 60)

    portfolio = [msft, aapl, spy]
    for asset in portfolio:
        print(asset.get_summary())