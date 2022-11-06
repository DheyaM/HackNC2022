# run this in terminal before running the notebook:
# pip install bs4
# pip install requests

from bs4 import BeautifulSoup
import requests
import pandas as pd
import plotly.express as px
import plot as plt

# #BIDEN:
# biden_promise = []
# url ='https://www.politifact.com/truth-o-meter/promises/list/?promise_group=biden-promise-tracker&ruling=promise-kept'
# response = requests.get(url)

# #print(response.status_code) # should be 200
# soup = BeautifulSoup(response.content, "html.parser")
# # element that contains the promises made
# results = soup.find_all("div", class_="m-statement__quote")

# data = []
# for result in results:
#     data.append(result.find('a'))

# #print(data)
# for d in data:
#     #print(str(d).split("\n")[1])
#     biden_promise.append(str(d).split("\n")[1])

# print("Number of fulfilled promises:",len(biden_promise))

# print("Biden has made 90 promises, out of which 22 have been kept")

# print(biden_promise)
# categories1 = ["healthcare","environmental","healthcare","other","other","other","other","healthcare","other","healthcare","environmental","other","other","other","healthcare","healthcare","other","other","other","healthcare","other","other"]

# #     #covid, medicaid, universal healthcare
# #     #Unemployment, Inflation, taxes (Sales and income tax)
# #     #(carbon (net 0), renewable energy, clean energy)
# #     #other

# # cats1 = ["covid","emissions","medicare","other","other","other","other","other","other","covid","assault","covid","other","other","covid","covid","other","other","other","other","other","other"]
# # print(len(cats1))

# # url ='https://www.politifact.com/truth-o-meter/promises/list/?page=1&promise_group=biden-promise-tracker&ruling=stalled'
# # response = requests.get(url)

# # print(response.status_code) # should be 200
# # soup = BeautifulSoup(response.content, "html.parser")
# # # element that contains the promises made
# # results = soup.find_all("div", class_="m-statement__quote")

# # data = []
# # for result in results:
# #     data.append(result.find('a'))

# # print(data)
# # for d in data:
# #     print(str(d).split("\n")[1])

# # print("Number of stalled promises:",len(data))
# # print(len(data))
# # cats2 = ["other","other","other","other","tax","other","other","other","other","other","other","prison","other","other","other","other","other","other","tuition","other","other","other","medicare","wage"]
# # print(len(cats2))

# #OBAMA:

# final_obama = []
# url = "https://www.politifact.com/truth-o-meter/promises/list/?promise_group=obameter&ruling=promise-kept"

# response = requests.get(url)

# # print(response.status_code) # should be 200
# soup = BeautifulSoup(response.content, "html.parser")
# # element that contains the promises made
# results = soup.find_all("div", class_="m-statement__quote")

# data = []
# for result in results:
#     data.append(result.find('a'))

# for d in data:
#     #print(str(d).split("\n")[1])
#     final_obama.append(str(d).split("\n")[1])

# # print("Number of met promises:",len(data))
# # print(len(data))
# # cats3 = ["other","other","other","other","tax","other","other","other","other","other","other","prison","other","other","other","other","other","other","tuition","other","other","other","medicare","wage"]
# # print(len(cats3))

# for i in range(2,12):
#     url = "https://www.politifact.com/truth-o-meter/promises/list/?page="+str(i)+"&promise_group=obameter&ruling=promise-kept"
#     response = requests.get(url)

#     # print(response.status_code) # should be 200
#     soup = BeautifulSoup(response.content, "html.parser")
#     # element that contains the promises made
#     results = soup.find_all("div", class_="m-statement__quote")

#     data = []
#     for result in results:
#         data.append(result.find('a'))

#     # print(data)
#     for d in data:
#         #print(str(d).split("\n")[1])
#         final_obama.append(str(d).split("\n")[1])
#     # print("Number of met promises for page"+str(i)+":",len(data))
#     # print(len(data))    

# print("Number of fulfilled promises:",len(final_obama))

# print("Obama has a total of 526 promises, 255 are met")

# #print(final_obama)
# categories2 = ["environment","other","other","environment","other","other","other","other","environment","other","education","other","other","other","other"] 

# final_trump= []
# url = "https://www.politifact.com/truth-o-meter/promises/list/?promise_group=trumpometer&ruling=promise-kept"
# response = requests.get(url)
# # print(response.status_code) # should be 200
# soup = BeautifulSoup(response.content, "html.parser")
# # element that contains the promises made
# results = soup.find_all("div", class_="m-statement__quote")
# data = []
# for result in results:
#     data.append(result.find('a'))

# # print(data)
# for d in data:
#     #print(str(d).split("\n")[1])
#     final_trump.append(str(d).split("\n")[1])
# # print("Number of met promises for page"+str(i)+":",len(data))
# # print(len(data))
# print("Number of fulfilled promises:",len(final_trump))
# print("Trump has a total of 102 promises, 24 of which have been met")
# print(final_trump)


#For NC State senators
#Thom Thillis: Healthcare: opiod addictiono crisis, health insurance for children, Transportation: funding general infrastructure, Broadband:
#Graig R Meyer: Healthcare: medicaid expeansion, Transportation: reduce carbon emission from transporation, Broadband:

df = pd.read_csv('presidential_promises-Sheet1.csv')
print(df)
df2 = df.groupby(['President','Category']).count()
just_pres = []
just_cat = []
for x in df2.index.to_list():
    just_pres.append(x[0])
    just_cat.append(x[1])
print(just_cat,just_pres)
df2["President"] = just_pres
df2["Categories"] = just_cat
    
print(df2)
count_df = pd.DataFrame(df['President'].value_counts())

def label_race (row):
    if row['President'] == "Biden" :
        return row['Promise']/count_df['President'][1]
    if row['President'] == "Obama" :
        return row['Promise']/count_df['President'][0]
    return row['Promise']/count_df['President'][2]


df4 = df2.apply(lambda row: label_race(row), axis=1)
print(type(df4))
print(df2)
print(df4)
df2["Values"] = df4
print(df2)

fig = px.bar(df2, x = 'Values', y = 'President', barmode = 'stack', color = 'Categories', hover_data=["Categories","Values"])
fig.show()