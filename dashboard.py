import streamlit as st
import pandas as pd
import plotly
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

st.sidebar.write("Write this to the sidebar")
playerName=st.sidebar.selectbox("Choose the Player",('Sachin Tendulkar','Virat Kohli'))

st.title(playerName)


# Player Data files
Player=pd.read_csv('D:\Projects\CricketPlayers\Players_Test_Data.csv')
PlayerData=Player.loc[Player['Name']==playerName,['Date','Runs','Balls','4s','6s','SR','Opponent','Inns_Total','Result']]
PlayerData=PlayerData.sort_values('Runs',ascending=False)

# Create the word cloud of the tendulkar
if playerName=='Sachin Tendulkar':
    ImageFileName='SachinTendulkar.png'
elif playerName=='Virat Kohli':
    ImageFileName='ViratKohli.jpg' 
else:
    ImageFileName='SachinTendulkar.png' 

Runs=PlayerData.loc[PlayerData['Runs'],:]
Runs.sort_values(by=['Runs'],inplace=True,ascending=False)
counts=Runs['Runs'].value_counts()
counts.index=sorted(counts.index)

IM1=Image.open(ImageFileName)
mask=np.array(IM1)

wordcloud=WordCloud(background_color='White',mask=mask,contour_color='black',contour_width=7).generate_from_frequencies(counts)

figure=plt.gcf()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.gca().set_position([0, 0, 1, 1])  

st.dataframe(PlayerData)