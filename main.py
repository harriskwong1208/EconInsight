import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px
from fredapi import Fred
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()

FredApiKey = os.getenv("Fred_Api_Key")


plt.style.use('fivethirtyeight')

#Lets us see up to 500 columns instead of the middle not being shown 
# pd.set_option('max_columns',500)

# List of color we can use to change the color of plot
color_pal = plt.rcParams['axes.prop_cycle'].by_key()['color']



print(FredApiKey)