import pandas as pd
import matplotlib.pyplot as plt


movies_df = pd.read_csv("/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/tmdb_movies.csv")
genres_df = pd.read_csv("/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/tmdb_genres.csv")


print("Kolumny w movies_df:", movies_df.columns)


movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
movies_df['release_year'] = movies_df['release_date'].dt.year


third_quartile = movies_df['vote_count'].quantile(0.75)


top_rated_movies = movies_df[(movies_df['vote_count'] > third_quartile)].sort_values(by='vote_average', ascending=False).head(10)
print("Top 10 najwyżej ocenianych filmów:", top_rated_movies[['title', 'vote_average', 'vote_count']])



filtered_movies = movies_df[(movies_df['release_year'] >= 2010) & (movies_df['release_year'] <= 2016)]


avg_revenue_budget = filtered_movies.groupby('release_year').agg({'revenue': 'mean', 'budget': 'mean'})


fig, ax = plt.subplots()


avg_revenue_budget['revenue'].plot(kind='bar', color='skyblue', ax=ax, position=1, width=0.4, label="Średni przychód")


avg_revenue_budget['budget'].plot(kind='line', color='orange', ax=ax, label="Średni budżet", marker='o')


ax.set_xlabel("Rok wydania")
ax.set_ylabel("Kwota (w miliardach)")
ax.set_title("Średni przychód i budżet filmów (2010-2016)")
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))  

plt.show()


merged_df = movies_df.merge(genres_df, how='left', left_on='genre_id', right_on=genres_df.columns[0])


most_common_genre = merged_df['genres'].value_counts().idxmax()
genre_count = merged_df['genres'].value_counts().max()
print(f"Najczęściej występujący gatunek to: {most_common_genre} ({genre_count} filmów)")


longest_runtime_genre = merged_df.groupby('genres')['runtime'].mean().idxmax()
longest_runtime = merged_df.groupby('genres')['runtime'].mean().max()
print(f"Gatunek o najdłuższym średnim czasie trwania to: {longest_runtime_genre} (średnio {longest_runtime:.2f} minut)")


genre_long_runtime = merged_df[merged_df['genres'] == longest_runtime_genre]['runtime']

plt.hist(genre_long_runtime.dropna(), bins=15, color='purple', edgecolor='black')
plt.xlabel('Czas trwania (minuty)')
plt.ylabel('Liczba filmów')
plt.title(f'Histogram czasu trwania dla gatunku: {longest_runtime_genre}')
plt.show()
