import pandas as pd
stock_prices = {
    "NVDA": 178.88,      
    "AAPL": 271.49,      
    "MSFT": 472.12,      
    "AMZN": 220.69,      
    "JPM": 298.02,       
    "TSLA": 391.09,      
    "WMT": 105.32        
}

name = input("Enter the stock name: ").upper()
quantity = int(input("Enter the quantity: "))
total = round(quantity*stock_prices[name],2)
print(f"Your total investment will be: {total}")
data = pd.DataFrame({
    "Stock Name" : [name],
    "Stock price" : stock_prices[name],
    "Quantity" : [quantity],
    "Total" : [total]
})
data.to_csv(r"C:/Users/DELL/Desktop/machine learning/CodeAlpha intership challenges/stocks.csv", index=None)
