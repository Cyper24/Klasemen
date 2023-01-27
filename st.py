import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time


st.text('Klasemen')

st.write('1. Liga Indonesia')
st.write('2. Liga inggris')
st.write('3. Liga Spanyol')
cari = st.text_input('What is it going', '')
    

if cari == '1':
        url = "https://prod-public-api.livescore.com/v1/api/app/stage/soccer/indonesia/liga-1/-5"
elif cari == '2':
        url = "https://prod-public-api.livescore.com/v1/api/app/stage/soccer/england/premier-league/-5"
elif cari == '3':
        url = 'https://prod-public-api.livescore.com/v1/api/app/stage/soccer/spain/laliga-santander/-5?'


try:
    response = requests.get(url)
    r= response.json()
    klas = []
    jm = len(r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'])
    for i in range(0,int(jm)):
        team = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['Tnm']
        play = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['pld']
        w = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['win']
        draw = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['drw']
        lost = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['drw']
        gf = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['gf']
        ga = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['ga']
        gd = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['gd']
        pts = r['Stages'][0]['LeagueTable']['L'][0]['Tables'][0]['team'][i]['pts']
        data = {'Team': team, 'P' : play,'W':w,'D':draw,'L':lost,'GF':gf,'GA':ga,'GD':gd,'PTS':pts}
        klas.append(data)
    df = pd.DataFrame(klas)
    df.index += 1
    st.dataframe(df, 1000, 500)
except:
        pass