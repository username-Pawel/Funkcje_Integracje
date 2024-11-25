from dash import dcc, html
import plotly.graph_objects as go

def render_tab(df):
    grouped = df[df['total_amt'] > 0].groupby('prod_cat')['total_amt'].sum()
    pie_fig = go.Figure(
        data=[go.Pie(labels=grouped.index, values=grouped.values)],
        layout=go.Layout(title='Udział grup produktów w sprzedaży')
    )

    layout = html.Div([
        html.H1('Produkty', style={'text-align': 'center'}),
        html.Div([
            html.Div([dcc.Graph(figure=pie_fig)], style={'width': '50%'}),
            html.Div([
                dcc.Dropdown(
                    id='prod_dropdown',
                    options=[{'label': cat, 'value': cat} for cat in df['prod_cat'].unique()],
                    value=df['prod_cat'].unique()[0]
                ),
                dcc.Graph(id='barh-prod-subcat')
            ], style={'width': '50%'})
        ], style={'display': 'flex'})
    ])
    return layout
