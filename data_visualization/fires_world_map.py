import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Data structure analysis
filename = 'data/fires_europe_real/MODIS_C6_1_Global_24h.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    lats, lons, brights, dates, times, hover_texts = [], [], [], [], [], []
    lats_index = header_row.index('latitude')
    lons_index = header_row.index('longitude')
    brights_index = header_row.index('brightness')
    dates_index = header_row.index('acq_date')
    times_index = header_row.index('acq_time')

    for row in reader:
        current_date_string = row[dates_index]
        current_time_string = row[times_index]
        current_datetime_string = current_date_string + ' ' + current_time_string
        current_date = datetime.strptime(current_datetime_string, '%Y-%m-%d %H%M')
        try:
            lat = float(row[lats_index])
            lon = float(row[lons_index])
            bright = float(row[brights_index])
        except ValueError:
            print(f'No data for date {current_date}.')
        else:
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)
            dates.append(current_date_string)
            times.append(current_time_string)
            hover_texts.append(current_date)

    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker': {
            'size': [0.05*bright for bright in brights],
            'color': brights,
            'colorscale': 'hot',
            'reversescale': False,
            'colorbar': {'title': 'Brightness'},
        },
    }]

    my_layout = Layout(title='Fires world map')

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='fires_world_map.html')

