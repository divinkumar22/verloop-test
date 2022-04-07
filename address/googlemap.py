import urllib
import requests
import json
import os 
from dotenv import load_dotenv
load_dotenv()

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'

def get_coordinates(address, from_sensor=False):
    final_result = {}
    key = os.getenv('api-key')
    url=f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}'
    r = requests.get(url)
    data = json.loads(r.content)
    results=data.get("results")[0].get("geometry").get("location")
    final_result["coordinates"] = results
    final_result['address'] = address
    return final_result
