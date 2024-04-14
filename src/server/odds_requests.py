### requests.py ###
"""
Handles all requests made to Odds API
"""

import requests
import os
from dotenv import load_dotenv


api_key = '96e0d8cee21660539bf27bc975f9ff26'

HOST = "https://api.the-odds-api.com"

def general_get_req(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Request failed with code: ", response.status_code, end="\n\n")
        return None

def sports_url():
    return HOST + f"/v4/sports/?apiKey={api_key}"

def odds_url(odds_dic):
    return (HOST +
        f'''/v4/sports/{odds_dic["sport_key"]}/odds/'''
        f'''?apiKey={api_key}'''
        f'''&regions={odds_dic["regions"]}'''
        f'''&markets={odds_dic["markets"]}''')
