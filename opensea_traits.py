import requests
from flask import jsonify
import json

with open('traits.json', 'w') as f:
  new_data = {}
  for i in range(1,10001):  
    url = "https://api.opensea.io/api/v1/asset/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/%d/" % (i)

    response = requests.request("GET", url)
    data = {i:json.loads(response.text)}
    
    for t in range(len(data[i]['traits'])):
      trait_count = data[i]['traits'][t]['trait_count']
      trait_type = data[i]['traits'][t]['trait_type']
      trait_value = data[i]['traits'][t]['value']
      if trait_type not in new_data:
        new_data[trait_type] = {}
      new_data[trait_type][trait_value] = trait_count
  json.dump(new_data, f)
f.close()