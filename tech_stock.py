from stock import Stock


class TechStock(Stock):
    PE_RATIO_BENCHMARK = 30
    GROWTH_FACTOR = 10
    def __init__(self, ticker: str, name: str, initial_price: float, pe_ratio: float):
        super().__init__(ticker, name, initial_price, "Technology")
        self.pe_ratio = pe_ratio

    def get_summary(self) -> str:
        base_info = super().get_summary()
        return f"{base_info} | Коефіцієнт P/E: {self.pe_ratio:.1f}"

    def forecast_growth(self, years: int):
        growth = (TechStock.PE_RATIO_BENCHMARK / self.pe_ratio) * TechStock.GROWTH_FACTOR
        print(f"-> Прогноз росту {self.ticker} на {years} років: {growth:.2f}%")
