# def visualize_state():
#     import plotly.express as px
#     return px.scatter(all_teams_df[all_teams_df.group == grpname], x='min_mid', y='player', size='shots_freq', color='pl_pps')

import pandas as pd
import numpy as np
import plotly.express as px

def graph():
    
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
    fig = px.bar(final_df, x = 'Value', y = 'Name', barmode = 'stack', color="Category", hover_data=["Name", "Value"])
    fig.update_xaxes(range=[0,3])
    return fig.show()
