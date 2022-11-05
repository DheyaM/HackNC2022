from bs4 import BeautifulSoup

import requests
import json 

# soup = BeautifulSoup(html_doc, 'html.parser')

url ='https://www.politifact.com/truth-o-meter/promises/list/?promise_group=biden-promise-tracker&ruling=promise-kept'
response = requests.get(url)
print(response.status_code) # should be 200
# convert json file
data_json = response.json()
print(type(data_json))
for x in data_json:
    print(x)
print("\n")