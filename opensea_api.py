import requests
from flask import jsonify
import json
import csv
import time
with open('trait_data_5000.json', 'w') as f:
  new_data = {}
  trait_data = {}
  for i in range(0,5000,1):
    url = "https://api.opensea.io/api/v1/asset/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/%d/" % (i)

    response = requests.request("GET", url)
    data = {i:json.loads(response.text)}

    #get pic id
    new_data[i] = {}
    trait_data[i] = {}
    new_data[i]['id'] = i
    #get pic price
    max_price = 0
    for j in range(len(data[i]['orders'])):
      price = float(data[i]['orders'][j]['current_price'])/1000000000000000000
      if data[i]['orders'][j]['payment_token_contract']['symbol'] == 'WETH':
        price = price * 4280.5
      max_price = max(max_price, price)
    #new_data[i]['price'] = max_price
    #get pic traits
    for t in range(len(data[i]['traits'])):
      key = data[i]['traits'][t]['trait_type']
      trait_data[i][key] = data[i]['traits'][t]['value']

    
    new_data[i]['Background'] = trait_data[i]['Background']
    new_data[i]['Fur'] = trait_data[i]['Fur']
    new_data[i]['Mouth'] = trait_data[i]['Mouth']
    new_data[i]['Eyes'] = trait_data[i]['Eyes']
    try:
      new_data[i]['Earring'] = trait_data[i]['Earring']
    except:
      new_data[i]['Earring'] = "None"
    try: 
      new_data[i]['Clothes'] = trait_data[i]['Clothes']
    except:
      new_data[i]['Clothes'] = "None"
    try:
      new_data[i]['Hat'] = trait_data[i]['Hat']
    except:
      new_data[i]['Hat'] = "None"
    print(i)
    time.sleep(1)
  json.dump(new_data, f, indent=1)

f.close()


dump_string = json.dumps(trait_data, indent=1)                                                      # outputs the contents of sales_json into text file
outF = open("trait_json.txt", "w")
outF.writelines(dump_string)
outF.close()


data_file = open('trait_data_file_5000.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0
 
    # Writing data of CSV file
for i in range(0,5000,1):     
  csv_writer.writerow(new_data[i].values())
  print("csv",i)
 
data_file.close()