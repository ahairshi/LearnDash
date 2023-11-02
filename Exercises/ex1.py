from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Select a State to Analyze', style={'textAlign': 'center'}),
    dcc.Dropdown(options=['California', 'Oregon', 'Washington'], id='dropdown-selection'),
    html.Br(),
    html.H3(id="country-output")
])


@callback(
    Output('country-output', 'children'),
    Input('dropdown-selection', 'value')
)
def update_state(value):
    if not value:
        raise PreventUpdate
    return f"State Selected: {value}"


if __name__ == '__main__':
    app.run(debug=True)
