import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

# Dane wejściowe
initial_price = 120000  # początkowa cena mieszkania w zł
price_increase_rate = 0.05  # roczny wzrost cen mieszkań
investment_years = 5  # okres inwestycji w latach
annual_nominal_rate = 0.12  # nominalna stopa procentowa banku
monthly_nominal_rate = annual_nominal_rate / 12  # miesięczna stopa nominalna
compounding_periods = investment_years * 12  # liczba miesięcy w okresie inwestycji

# 1. Obliczenie ceny mieszkania po 5 latach
final_price = initial_price * (1 + price_increase_rate) ** investment_years

# 2. Obliczenie miesięcznej wpłaty do banku, aby osiągnąć wartość mieszkania po 5 latach
# FV = kwota końcowa, PMT = rata miesięczna, i = stopa miesięczna, n = liczba miesięcy
# FV = PMT * ((1 + i)^n - 1) / i
monthly_payment = npf.pmt(rate=monthly_nominal_rate, nper=compounding_periods, pv=0, fv=-final_price, when='end')

# 3. Tworzenie wykresu: wartość mieszkania i stan lokaty w czasie
months = np.arange(1, compounding_periods + 1)
monthly_price_increase = initial_price * (1 + price_increase_rate) ** (months / 12)
investment_balance = npf.fv(rate=monthly_nominal_rate, nper=months, pmt=-monthly_payment, pv=0, when='end')

# Wykres
plt.figure(figsize=(12, 6))
plt.plot(months, monthly_price_increase, label="Cena mieszkania", color='blue', linestyle='--')
plt.plot(months, investment_balance, label="Stan lokaty", color='green')
plt.xlabel("Miesiące")
plt.ylabel("Wartość (zł)")
plt.title("Zmiana ceny mieszkania i wartości lokaty w czasie")
plt.legend()
plt.grid(True)
plt.show()

# Wyniki 
print(final_price, -monthly_payment)

# Orientacyjna cena miszkań za 5 lat: 153 153,79zł. 
# Wymagana miesięczna wpłata do banku: 1875,28zł.