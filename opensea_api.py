import requests
from flask import jsonify
import json
import csv
with open('data.json', 'w') as f:
  new_data = {}
  for i in range(1,11):  
    url = "https://api.opensea.io/api/v1/asset/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/%d/" % (i)

    response = requests.request("GET", url)
    data = {i:json.loads(response.text)}

    #get pic id
    new_data[i] = {}
    new_data[i]['id'] = i
    #get pic price
    max_price = 0
    for j in range(len(data[i]['orders'])):
      price = float(data[i]['orders'][j]['current_price'])/1000000000000000000
      if data[i]['orders'][j]['payment_token_contract']['symbol'] == 'WETH':
        price = price * 4280.5
      max_price = max(max_price, price)
    new_data[i]['price'] = max_price
    #get pic traits
    new_data[i]['traits'] = []
    for t in range(len(data[i]['traits'])):
      new_data[i]['traits'].append(data[i]['traits'][t]['trait_count'])
  json.dump(new_data, f)
f.close()


data_file = open('data_file.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0
 
    # Writing data of CSV file
for i in range(1,11):     
  csv_writer.writerow(new_data[i].values())
 
data_file.close()