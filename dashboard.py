from pie import pie_plot
from bar import bar_plot
from scatter import scatter_plot

import chart_studio.plotly as py
import re
import chart_studio.dashboard_objs as dashboard

import chart_studio

chart_studio.tools.set_credentials_file(username='kategera6', api_key='Y27sZ8nv85xKg4Bx3x1X')


def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+[/0-9]+", url)[0][1:]
    return raw_fileId.replace('/', ':')

my_dboard = dashboard.Dashboard()

bar_plot_id = fileId_from_url(bar_plot)
pie_plot_id = fileId_from_url(pie_plot)
scatter_plot_id = fileId_from_url(scatter_plot)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_plot_id,
    'title': 'genre name and number of songs'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_plot_id,
    'title': 'artist name and songs percentile'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_plot_id,
    'title': 'loudness and popularity'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'My Workshop2 Plots')