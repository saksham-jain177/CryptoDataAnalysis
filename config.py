from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("CMC_API_KEY")
API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
