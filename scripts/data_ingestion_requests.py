import os
import requests
from dotenv import load_dotenv

load_dotenv

api_key = os.getenv("POKEMON_API_KEY")

headers = {
    'X-Api-Key': api_key,
}

response = requests.get('https://api.pokemontcg.io/v2/cards/xy1-1', headers=headers)

print(response.status_code)
print(response.text)