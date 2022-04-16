
from dash import Dash, dcc, html
import dash
import dash_table
from dash.dependencies import Input,Output
import dash_bootstrap_components as dbc



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])
server=app.server


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    dcc.Link('Page 1: Filter Table', href='/page-1'),
    html.Br(),
    dcc.Link('Page 2: Summary Table', href='/page-2'),
    html.Br(),
    dcc.Link('Page 3: Dash', href='/page-3'),
    html.Br(),
    dcc.Link('Page 4: Drag & Drop Hourly Report', href='/page-4'),
])

'''######################################### Page 1 ###############################'''
page_1_layout = html.Div([
    html.H1('Page 1: Filter Data'),
    html.Div(

        children=[
            html.Div('Filtered Dash Board',
                     style={
                         'height': '50px',
                         'font-size': '25px',
                         'font-family': 'Georgia',
                         'text-align': "left",
                         'display': 'block',
                         'width': '22%',
                     }
                     ),
            dcc.Dropdown(
                id='Date_dropdown',
                value="Date",
                placeholder="Date",
                style={'color': "Black", 'background-color': 'darkcyan', 'font-size': '25px', 'display': 'inline-block',
                       'width': '50%'}
            ),  # 'border-radius':'4px'

            dcc.Dropdown(
                id='Unit_dropdown',
                value="Unit",
                placeholder="Unit",
                style={'color': "Black", 'background-color': 'darkcyan', 'font-size': '25px', 'display': 'inline-block',
                       'width': '50%'}
            ),

            dcc.Dropdown(
                id='Style_dropdown',
                value="Style",
                placeholder="Style",
                style={'color': "Black", 'background-color': 'darkcyan', 'font-size': '15px', 'display': 'inline-block',
                       'width': '50%'}
            ),

            dcc.Dropdown(
                id='Line_dropdown',
                value="Line",
                placeholder="Line",
                style={'color': "Black", 'background-color': 'darkcyan', 'font-size': '25px', 'display': 'inline-block',
                       'width': '50%'}
            ),

            dash_table.DataTable(
                id='table-container',
                style_cell_conditional=[
                    {
                        'color': "Black",
                        'font-size': '20px',
                        'text-align': "center",
                        'background-color': 'darkcyan',
                        'border-style': 'solid',
                    }
                ],
            )
        ],

    ),

    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])

page_2_layout = html.Div([])
page_3_layout = html.Div([])

page_4_layout = html.Div([])

''' ##################################### FUNCTIONS ##########################################'''




@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-4':
        return page_4_layout
    else:
        return index_page



if __name__ == '__main__':
    app.run_server(debug=False)