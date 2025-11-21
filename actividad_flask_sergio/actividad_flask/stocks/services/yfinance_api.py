import yfinance as yf

def get_stock_quote(symbol: str):
    """
    Retrieves basic stock info from yfinance.
    """
    ticker = yf.Ticker(symbol)

    # fast_info is lightweight and fast
    info = ticker.fast_info

    return {
        "symbol": symbol,
        "last_price": info.get("lastPrice"),
        "currency": info.get("currency"),
        "exchange": info.get("exchange"),
        "previous_close": info.get("previousClose"),
        "open": info.get("open"),
        "day_high": info.get("dayHigh"),
        "day_low": info.get("dayLow"),
    }
