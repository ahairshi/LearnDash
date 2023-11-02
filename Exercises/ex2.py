import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

education = pd.read_csv("../Data/states_all.csv", usecols=["STATE", "YEAR", "TOTAL_EXPENDITURE"])

app=Dash(__name__)
app.layout = html.Div([
    html.H1(children='Select a State to Analyze', style={'textAlign': 'center'}),
    dcc.Dropdown(options=education.STATE.unique(), id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(state):
    if state is None:
        raise PreventUpdate
    df = education.query(f"STATE == '{state.upper()}' & YEAR > 1992")
    return px.line(
        df, 
        x='YEAR', 
        y='TOTAL_EXPENDITURE',
        markers=True,
        title=f"Expenditure in {state.title()}")


if __name__ == '__main__':
    app.run(debug=True)