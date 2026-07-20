import os
import requests
from dotenv import load_dotenv

load_dotenv

api_key = os.getenv("POKEMON_API_KEY")

headers = {
    'X-Api-Key': api_key,
}

BASEURL = 'https://api.pokemontcg.io/v2'

def sendRequest(requestURL):
    response = requests.get(requestURL, headers=headers)
    return response.text

def getPokemonByName(name):
    cardQuery = '/cards?q=name:'
    pokemon = f'"{name}"'
    requestURL = BASEURL + cardQuery + pokemon
    return sendRequest(requestURL)

def getSetByName(name):
    cardQuery = '/sets?q=name:'
    set = f'"{name}"'
    requestURL = BASEURL + cardQuery + set
    print(requestURL)
    return sendRequest(requestURL)