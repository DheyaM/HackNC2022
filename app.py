from flask import Flask, render_template, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from wtforms import Form, TextAreaField, validators, StringField, SubmitField
from flask import Flask, redirect, url_for, request
from twilio.rest import Client
import os
import pandas as pd
import numpy as np
import plotly.express as px
from plotly import utils
from json import dumps
import json
import plotly
import plotly.express as px


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/federal')
def federal():
    return graph1()

@app.route('/national')
def national():
    return graph2()

@app.route('/national')
def graph2():
    df = pd.read_csv('presidential_promises-Sheet1.csv')
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
    df2["Values"] = df4

    fig = px.bar(df2, x = 'Values', y = 'President', barmode = 'stack', color = 'Categories', hover_data=["Categories","Values"])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('national.html', graphJSON=graphJSON)

@app.route('/federal')
def graph1():
    
    df = pd.read_csv('table.csv')
    print(df)
    print(type(df['public_transport_funding_start']))

    def transportation(row):
        if (np.isnan(row['public_transport_funding_start'])):
            if (row['road_pred'] < row['road_today']):
                return 1
            return 0
        trans_fund_percent = 100*(row['public_transport_funding_today'] - row['public_transport_funding_start'])/row['public_transport_funding_start']
        road_fund_percent = 100*(row['road_pred'] - row['road_today'])/row['road_pred']
        # if the average percent in funding is positive, then the promise is met
        if ((trans_fund_percent + road_fund_percent)>0):
            return 1
        return 0

    def education(row):
        if row['HBCU_funding_start'] < row['HBCU_funding_end']:
            return 1
        return 0

    def socioeconomic(row):
        if row['broadband_access_start'] < row['broadband_access_today']:
            return 1
        return 0

    df['education'] = df.apply(lambda row : education(row), axis=1) 
    df['socioeconomic'] = df.apply(lambda row : socioeconomic(row), axis=1) 
    df['transportation'] = df.apply(lambda row : transportation(row), axis=1) 

    print(df)

    # Person 1 dataframe to plot
    df_mod = pd.DataFrame()
    df_mod['Category'] = list(df.columns[-3:])
    df_mod['Category'] = df_mod['Category'].astype(str)
    df_mod['Name'] = df['name'][0]
    df_mod['Value'] = 0
    for ind in df_mod.index:
        if df_mod['Category'][ind] == 'transportation':
            df_mod['Value'][ind] = df['transportation'][0]
        elif df_mod['Category'][ind] == 'education':
            df_mod['Value'][ind] = df['education'][0]
        else:
            df_mod['Value'][ind] = df['socioeconomic'][0]

    # df_mod['Value'] = np.where(df_mod['Category'] == 'transportation', df['transportation'][0], -1)
    # df_mod['Value'] = np.where(df_mod['Category'] == 'education', df['education'][0], -1)
    # df_mod['Value'] = np.where(df_mod['Category'] == 'socioeconomic', df['socioeconomic'][0], -1)

    # Person 2 dataframe to plot
    df_mod2 = pd.DataFrame()
    df_mod2['Category'] = list(df.columns[-3:])
    df_mod2['Category'] = df_mod2['Category'].astype(str)
    df_mod2['Name'] = df['name'][1]
    df_mod2['Value'] = 0
    for ind in df_mod2.index:
        if df_mod2['Category'][ind] == 'transportation':
            df_mod2['Value'][ind] = df['transportation'][1]
        elif df_mod2['Category'][ind] == 'education':
            df_mod2['Value'][ind] = df['education'][1]
        else:
            df_mod2['Value'][ind] = df['socioeconomic'][1]

    final_df = pd.concat([df_mod, df_mod2], sort=False)
    print(final_df)

    df['Counts'] = df['education'] + df['transportation'] + df['socioeconomic']
    color_disc_map = {"education":"purple", "socioeconomic":"orange"}
    fig = px.bar(final_df, x = 'Value', y = 'Name', barmode = 'stack', color="Category", hover_data=["Name", "Value"], color_discrete_map = color_disc_map)
    fig.update_xaxes(range=[0,3])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('federal.html', graphJSON=graphJSON)

@app.route('/contact',methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':

      account_sid = 'ACd9d4915d24ff185747928709fc090ab6'
      auth_token = '589df6881c26ebb8a666d6c82986239f'

      client = Client(account_sid, auth_token)

      client.messages.create(from_='+13023052770',
                      to=request.form["phone name"],
                      body='Thanks for signing up for text messages. We will updata you on the progress of promises made by elected officials.' +
                      'Here is the voting registration link: https://www.ncdot.gov/dmv/offices-services/online/Pages/voter-registration-application.aspx'
                      'Address of Nearby Voting Registration: 208 S. Cameron Street PO Box 220 Hillsborough, NC 27278, Phone: 919-245-2350')
      
   return render_template("thanks.html")
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 4040)