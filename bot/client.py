import os
from binance.client import Client

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise Exception("API key or secret not found in environment variables")

        self.client = Client(api_key, api_secret)
        self.client.API_URL = "https://testnet.binance.vision/api"

