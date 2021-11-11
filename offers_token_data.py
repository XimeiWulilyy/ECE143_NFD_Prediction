import requests
from flask import jsonify
import json
import csv
import time
with open('trait_data_file_with_offer.json', 'w') as f:
  new_data = {}
  for ids in range(0,10000):
    url_offer = "https://api.opensea.io/api/v1/asset/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/%d/" % (ids)
    url_sales = "https://api.opensea.io/api/v1/events?asset_contract_address=0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d&token_id=%d&event_type=successful" % (ids)
    response_offer = requests.request("GET", url_offer)
    response_sales = requests.request("GET", url_sales)
    response_sales = response_sales.json()
    data = {ids:json.loads(response_offer.text)}

    #get pic id
    new_data[ids] = {}
    new_data[ids]['id'] = ids
    #get pic price
    latest_price = 0
    # for j in range(len(data[ids]['orders'])):
    # if data[ids]['orders'][0]['payment_token_contract']['symbol'] == 'WETH':
    if len(data[ids]['orders']) != 0:
      latest_price = float(data[ids]['orders'][0]['current_price'])/1000000000000000000
    new_data[ids]['price'] = latest_price
    e = len(response_sales['asset_events'])
    for i in range(e):
      sale_price = int(response_sales['asset_events'][e-1-i]['total_price'])/1000000000000000000                                                  
      new_data[ids]['sales%d' % (ids)] = sale_price
  json.dump(new_data, f, indent=1)

f.close()


# dump_string = json.dumps(new_data, indent=1)                                                      # outputs the contents of sales_json into text file
# outF = open("trait_json.txt", "w")
# outF.write(dump_string)
# outF.close()


data_file = open('trait_data_file_with_offer.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
count = 0
    # Writing data of CSV file
for i in range(0,10000):     
  csv_writer.writerow(new_data[i].values())
data_file.close()