from dash import dcc, html
import plotly.graph_objects as go

def render_tab(df):
    df['day_of_week'] = df['tran_date'].dt.day_name()
    sales_by_day = df.groupby(['day_of_week', 'Store_type'])['total_amt'].sum().unstack().fillna(0)
    sales_by_day = sales_by_day.loc[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]

    bar_traces = [
        go.Bar(x=sales_by_day.index, y=sales_by_day[col], name=col) for col in sales_by_day.columns
    ]

    sales_fig = go.Figure(data=bar_traces, layout=go.Layout(title='Sprzedaż według dnia tygodnia', barmode='stack'))

    layout = html.Div([
        html.H1('Kanały sprzedaży', style={'text-align': 'center'}),
        dcc.Graph(figure=sales_fig)
    ])
    return layout
