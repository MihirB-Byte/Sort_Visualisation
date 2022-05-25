import pandas as pd
from plotly.tools import mpl_to_plotly
import dash_core_components as dcc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
import matplotlib.colors as mc
import colorsys
from random import randint
import plotly.tools as tls
import re
import plotly.graph_objects as go

data = pd.read_csv('table.csv', usecols=['Country_Name','Years','Ratio GDP', 'Continent_Name','Receipts_PCapita'])




