from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

"""
# Impact of environmental factors on public health using spatial analysis

##### Asthma

Around 8% of the US population suffers from asthma. Asthma has become one of the most prevalent diseases in the US, 
sending over 1.2 million people annauully to the emergency room

##### Our proposal
A geospatial correlation map between pollutants and asthma rates. We certanly know that asthma is not caused bu just one factor but it can be influenced by many.
Our goal will be show how diffferent polutants in the air affect asthma rate with correlations.


"""

data = pd.read_csv('Cali2018Form.csv')
print(data)

# Sidebar options
st.sidebar.header('Regression Parameters')
slope = st.sidebar.slider('Slope', 8.0, 10.0, 1.0)
intercept = st.sidebar.slider('Intercept', 7.0, 10.0, 0.0)

# Scatter plot and regression line
fig, ax = plt.subplots()
ax.scatter(data['form'], data['prev18'])
ax.plot(data['form'], slope*data['form'] + intercept, color='red')
ax.set_xlabel('Form')
ax.set_ylabel('Prev18')

# Calculate MSE
predicted = slope*data['form'] + intercept
mse = np.mean((data['prev18'] - predicted)**2)
# st.write('Mean Squared Error:', mse)

# Display MSE
mse_text = f'MSE: {mse:.2f}'
bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1)
ax.text(0.95, 0.95, mse_text, transform=ax.transAxes, fontsize=10, va='top', ha='right', bbox=bbox_props)

st.pyplot(fig)
