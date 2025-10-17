from stock import Stock
from portfolio_holder import PortfolioHolder


class EtfFund(Stock, PortfolioHolder):
    def __init__(self, ticker: str, name: str, initial_price: float, asset_count: int):
        Stock.__init__(self, ticker, name, initial_price, "Fund")
        PortfolioHolder.__init__(self)
        self.asset_count = asset_count

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