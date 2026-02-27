from flask import Flask, request
import requests
import os

app = Flask(__name__)

FYERS_TOKEN = os.environ.get("FYERS_TOKEN")
WATCHLIST = "Chartink"

@app.route('/')
def home():
return "Running"

@app.route('/webhook', methods=['POST'])
def webhook():
data = request.json
try:
stock = data["stocks"]
symbol = f"NSE:{stock}-EQ"

url = "https://api.fyers.in/api/v2/watchlist/add-symbol"
headers = {
"Authorization": FYERS_TOKEN,
"Content-Type": "application/json"
}

payload = {
"symbol": symbol,
"watchlist_name": WATCHLIST
}

r = requests.post(url, json=payload, headers=headers)
print(r.text)

except Exception as e:
print(e)

return "ok"

if __name__ == "__main__":
app.run(host="0.0.0.0", port=10000)
