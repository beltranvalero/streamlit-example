from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

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
slope = st.sidebar.slider('Slope', -10.0, 10.0, 1.0)
intercept = st.sidebar.slider('Intercept', -10.0, 10.0, 0.0)

# Scatter plot and regression line
fig, ax = plt.subplots()
ax.scatter(data['form'], data['prev18'])
ax.plot(data['form'], slope*data['form'] + intercept, color='red')
ax.set_xlabel('Form')
ax.set_ylabel('Prev18')
st.pyplot(fig)

# Calculate MSE
predicted = slope*data['form'] + intercept
mse = np.mean((data['prev18'] - predicted)**2)
st.write('Mean Squared Error:', mse)



with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
