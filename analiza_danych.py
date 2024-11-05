import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/HRDataset.csv')


print(df.head())
print(df.columns)


plt.figure(figsize=(10, 6))
df.groupby('ManagerName')['PerformanceScore'].value_counts().unstack().plot(kind='bar', stacked=True)
plt.title('Ocena wydajności w zależności od menedżera')
plt.xlabel('Menedżer')
plt.ylabel('Liczba pracowników')
plt.legend(title='Ocena wydajności')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


df['DateofHire'] = pd.to_datetime(df['DateofHire'])
df['Tenure'] = (pd.Timestamp.now() - df['DateofHire']).dt.days

plt.figure(figsize=(10, 6))
avg_tenure_by_source = df.groupby('RecruitmentSource')['Tenure'].mean().sort_values()
avg_tenure_by_source.plot(kind='barh')
plt.title('Średni staż pracowników w zależności od źródła pozyskania')
plt.xlabel('Średni staż (dni)')
plt.ylabel('Źródło pozyskania')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
df.groupby('MaritalDesc')['EmpSatisfaction'].mean().plot(kind='bar')
plt.title('Zadowolenie z pracy w zależności od stanu cywilnego')
plt.xlabel('Stan cywilny')
plt.ylabel('Średnie zadowolenie z pracy')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


df['DOB'] = pd.to_datetime(df['DOB'], format='%m/%d/%Y', errors='coerce')
df['Age'] = (pd.Timestamp.now() - df['DOB']).dt.days // 365

plt.figure(figsize=(10, 6))
df['Age'].hist(bins=20)
plt.title('Struktura wieku zatrudnionych pracowników')
plt.xlabel('Wiek')
plt.ylabel('Liczba pracowników')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
df.groupby('Age')['SpecialProjectsCount'].mean().plot(kind='line')
plt.title('Średnia liczba specjalnych projektów w zależności od wieku')
plt.xlabel('Wiek')
plt.ylabel('Średnia liczba projektów')
plt.tight_layout()
plt.show()
