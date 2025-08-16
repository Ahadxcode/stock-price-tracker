
import yfinance as yf
import matplotlib.pyplot as plt

def stock_tracker(symbol, period="6mo"):
    """
    Fetch and plot stock data.
    symbol: Stock ticker (e.g., 'AAPL', 'TSLA', 'RELIANCE.NS')
    period: Time period (e.g., '1mo', '3mo', '6mo', '1y')
    """

    # Fetch stock data
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)

    if data.empty:
        print("❌ No data found. Check the symbol or period.")
        return

    # Basic statistics
    print(f"\n📊 Stock Analysis for {symbol}")
    print(f"Time Period: {period}")
    print(f"Max Price: {data['Close'].max():.2f}")
    print(f"Min Price: {data['Close'].min():.2f}")
    print(f"Average Price: {data['Close'].mean():.2f}")

    # Plot closing prices
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label="Closing Price", color="blue")
    plt.title(f"{symbol} Stock Price ({period})")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()


# Example Run
if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA, RELIANCE.NS): ")
    period = input("Enter period (1mo, 3mo, 6mo, 1y): ")
    stock_tracker(symbol, period)


# In[ ]:




