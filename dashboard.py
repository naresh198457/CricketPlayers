import streamlit as st
import pandas as pd
import plotly
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.sidebar.write("Write this to the sidebar")
playerName=st.sidebar.selectbox("Choose the Player",('Sachin Tendulkar','Virat Kohli'))

st.title(playerName)


# Player Data files
Player=pd.read_csv('Players_Test_Data.csv')
PlayerData=Player.loc[Player['Name']==playerName,['Date','Runs','Balls','4s','6s','SR','Opponent','Inns_Total','Result']]
PlayerData=PlayerData.sort_values('Runs',ascending=False)

# Create the word cloud of the tendulkar



st.dataframe(PlayerData)