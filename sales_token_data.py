import requests
import json
with open('response.txt', 'w') as f:
    sales_data = {}
    
    for ids in range (9999):
        url = "https://api.opensea.io/api/v1/events?asset_contract_address=0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d&token_id=%d&event_type=successful" % (ids)
 
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers)

        response = response.json()
        sales_data[ids] = {}
        sales_data[ids]['id'] = ids

        e = len(response['asset_events'])
        print(e)
        sales_data[ids]['sales'] = []
        for i in range(e):
            sale_price = int(response['asset_events'][e-1-i]['total_price'])/1000000000000000000
            time_stamp = response['asset_events'][e-1-i]['transaction']['timestamp']                                                     
            sales_data[ids]['sales'].append((sale_price,time_stamp))
            
    json.dump(sales_data, f, indent =1)
f.close()
        





