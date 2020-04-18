import chart_studio.plotly as py
import plotly.graph_objs as go

from queries import data1

genre_name = data1['GENRE_NAME']
num_of_songs = data1['NUM_OF_SONGS']

data = [go.Bar(
    x=genre_name,
    y=num_of_songs
)]

layout = go.Layout(
    title='genre name and number of songs',
    xaxis=dict(
        title='genre name',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='number of songs',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)

bar_plot = py.plot(fig, filename='genre_name-num_of_songs')
print(bar_plot)