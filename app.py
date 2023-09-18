import dash
# import dash_core_components as dcc
# import dash_html_components as html
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd

# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dcc.Graph(id='scatter-plot'),
    dcc.Slider(
        id='slider',
        min=1,
        max=5,
        step=1,
        value=3,
        marks={i: str(i) for i in range(1, 6)}
    )
])

# Define callback to update the scatter plot


@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('slider', 'value')]
)
def update_graph(selected_value):
    filtered_df = df[df['x'] <= selected_value]
    fig = {
        'data': [
            {'x': filtered_df['x'], 'y': filtered_df['y'],
                'type': 'scatter', 'mode': 'lines+markers'}
        ],
        'layout': {
            'title': f'Scatter Plot (X <= {selected_value})'
        }
    }
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8050)
