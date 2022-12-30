import dash
from dash import dcc

from dash import html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Croissance de la température en france et dans le monde :'),

    html.Div(children='''
        Dash : un framework pour la création de dashboards en Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Données de test'
            }
        }
    )
])

if __name__ == '__main__':
    print()
    app.run_server(debug=True)
    print("test")