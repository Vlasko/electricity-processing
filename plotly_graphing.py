# Standard Library Imports
import os

# Third Party Imports
from plotly.offline import plot
import plotly.graph_objs as go

from functions.cleaning_functions import clean_demand, clean_price

directory = os.getcwd()

demand_path = directory+'/files/demand/'
demand_df = clean_demand(demand_path)

price_path = directory+'/files/prices/'
price_df = clean_price(price_path)

fig = go.Figure(go.Scatter(x=demand_df.index, y=demand_df.iloc[:,0]))
fig.show()

plt_div = plot(fig, output_type='div') 
