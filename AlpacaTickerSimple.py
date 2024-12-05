from AlpacaApiKey import API_KEY_ID, API_SECRET_KEY
import requests

# Create the headers dictionary with correct keys and values
headers = {
    "APCA-API-KEY-ID": API_KEY_ID,
    "APCA-API-SECRET-KEY": API_SECRET_KEY,
    "accept": "application/json"
}

symbol = input('Enter Stock symbol to request data : ')
period = input('Enter time Period (1, 5, 10, 15, 30) : ')

# URL for the Alpaca API
url = f"https://data.alpaca.markets/v2/stocks/bars?symbols={symbol}&timeframe={period}min&limit=1000&adjustment=raw&feed=sip&sort=asc"

# Make the GET request
response = requests.get(url, headers=headers)

# Print the response
#print(response.json())  # Assuming JSON response

data_json = response.json()
#print(f"data_json = {data_json}")

data_stock = data_json['bars'][symbol]
#print(f"data_json = {data_stock}")

for ohlcv_data in data_stock:
    #print(f"ohlcv_data = {ohlcv_data}") 
    c_data : str = []
    c_data = ohlcv_data['c']
    #print(f"c_data = {c_data}")
    
    #inner_data = c_data.split(",")
    #print(f"inner_data = {inner_data}")
    
    print(f"Close: {ohlcv_data['c']}, High: {ohlcv_data['h']}, Low: {ohlcv_data['l']}, "
    f"Number of trades: {ohlcv_data['n']}, Open: {ohlcv_data['o']}, "
    f"Timestamp: {ohlcv_data['t']}, Volume: {ohlcv_data['v']}, VWAP: {ohlcv_data['vw']}")
