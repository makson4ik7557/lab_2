from stock import Stock
from tech_stock import TechStock
from etf_fund import EtfFund

if __name__ == "__main__":
    msft = Stock("MSFT", "Microsoft Corp", 420.00, "Technology")
    jnj = Stock("JNJ", "Johnson & Johnson", 155.50, "Healthcare")
    aapl = TechStock("AAPL", "Apple Inc.", 175.00, 35.5)
    spy = EtfFund("SPY", "S&P 500 ETF", 520.00, 500)

    print("=" * 60)
    print(f"*** РИНОК: {Stock.get_exchange_name()} ***")
    print("=" * 60)

    print(f"Початкова ціна {aapl.ticker}: ${aapl.current_price:.2f}")

    aapl.current_price = 180.50
    aapl.current_price = 0
    print(f"Поточна ціна {aapl.ticker} після помилки: ${aapl.current_price:.2f}")

    print(f"Активів для {msft.ticker} (нестатичний лічильник): {msft.total_assets_tracked}")
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
