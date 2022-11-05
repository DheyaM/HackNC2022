from bs4 import BeautifulSoup

import requests
import json

# soup = BeautifulSoup(html_doc, 'html.parser')

url ='https://www.politifact.com/truth-o-meter/promises/list/?promise_group=biden-promise-tracker&ruling=promise-kept'
response = requests.get(url)

print(response.status_code) # should be 200
soup = BeautifulSoup(response.content, "html.parser")
print(soup)
# element that contains the promises made
results = soup.find_all("div", class_="m-statement__quote")
print(results)
print(type(results))

# data = json.loads(response.text)[0]

data = []

for result in results:
    data.append(result.find('a'))

print(data)
print(type(data))
print(data[1])