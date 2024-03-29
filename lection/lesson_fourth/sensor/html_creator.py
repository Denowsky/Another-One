from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):
    style = 'style="front-size:30px"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}> Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '    <p {}> Pressure: {} c</p>\n'\
        .format(style, pressure_view(device))
    html += '    <p {}> Wind_speed: {} c</p>\n'\
        .format(style, wind_speed_view(device))
        
    with open('index.html', 'w') as page:
        page.write(html)
    return html