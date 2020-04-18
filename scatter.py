from queries import data3
import chart_studio.plotly as py
import plotly.graph_objs as go

popularity = data3['POPULARITY']
loudness = data3['LOUDNESS']

data = go.Scatter(
    x=loudness,
    y=popularity,
    mode='lines+markers'
)
data = [data]
scatter_plot = py.plot(data, filename='loudness-popularity')