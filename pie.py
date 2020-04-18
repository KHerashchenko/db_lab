from queries import data2
import chart_studio.plotly as py
import plotly.graph_objs as go

artist_name = data2['ARTIST_NAME']
songs_percentile = data2['SONGS_PERCENTILE']

pie = go.Pie(labels=artist_name, values=songs_percentile)
pie_plot = py.plot([pie], filename='artist_name-songs_percentile')