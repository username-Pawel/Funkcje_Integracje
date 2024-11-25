from dash import Dash, dcc, html, Input, Output
import tab1, tab2, tab3
import pandas as pd
import os
import datetime as dt

# Inicjalizacja aplikacji
app = Dash(__name__, suppress_callback_exceptions=True)

# Klasa do obsługi danych
class db:
    def __init__(self):
        self.transactions = self.transaction_init()
        self.cc = pd.read_csv('/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/db/country_codes.csv', index_col=0)
        self.customer = pd.read_csv('/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/db/customers.csv', index_col=0)
        self.prod_info = pd.read_csv('/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/db/prod_cat_info.csv')

    def transaction_init(self):
        transactions = pd.DataFrame()
        src = '/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/db/transactions'
        for filename in os.listdir(src):
            if filename.endswith('.csv'):
                transactions = pd.concat([transactions, pd.read_csv(os.path.join(src, filename))], ignore_index=True)

        def convert_dates(x):
            try:
                return dt.datetime.strptime(x, '%d-%m-%Y')
            except:
                return dt.datetime.strptime(x, '%d/%m/%Y')

        transactions['tran_date'] = transactions['tran_date'].apply(convert_dates)
        return transactions

    def merge(self):
        df = self.transactions.join(
            self.prod_info.drop_duplicates(subset=['prod_cat_code']).set_index('prod_cat_code')['prod_cat'],
            on='prod_cat_code',
            how='left'
        ).join(
            self.prod_info.drop_duplicates(subset=['prod_sub_cat_code']).set_index('prod_sub_cat_code')['prod_subcat'],
            on='prod_subcat_code',
            how='left'
        ).join(
            self.customer.join(self.cc, on='country_code').set_index('customer_Id'),
            on='cust_id'
        )
        self.merged = df

# Przygotowanie danych
df = db()
df.merge()

# Layout aplikacji
app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Sprzedaż globalna', value='tab-1'),
        dcc.Tab(label='Produkty', value='tab-2'),
        dcc.Tab(label='Kanały sprzedaży', value='tab-3'),
    ]),
    html.Div(id='tabs-content')
])

# Callback do przełączania zakładek
@app.callback(Output('tabs-content', 'children'), [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1.render_tab(df.merged)
    elif tab == 'tab-2':
        return tab2.render_tab(df.merged)
    elif tab == 'tab-3':
        return tab3.render_tab(df.merged)

if __name__ == '__main__':
    app.run_server(debug=True)
