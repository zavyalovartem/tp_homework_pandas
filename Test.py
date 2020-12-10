import pandas as pd
from itertools import islice

df = pd.read_csv("netflix_titles.csv")


# Самые длинные сериалы
def get_longest_running_shows(df):
    df_shows = df[(df['type'] == "TV Show")]
    df_shows = df_shows[['title', 'duration']]
    df_shows['duration'] = df_shows['duration'].str.split(' ', expand=True)
    df_shows['duration'] = pd.to_numeric(df_shows['duration'])
    df_shows = df_shows.sort_values(by='duration', ascending=False)
    res = pd.Series(df_shows.duration.values, index=df_shows.title).to_dict()
    res = dict(islice(res.items(), 10))
    for key in res.keys():
        print(key + ': ' + str(res[key]) + ' seasons')


# Случайные 3 британских фильма с рейтингом PG
def get_random_pg(df):
    df_movies = df[(df['type'] == 'Movie') & (df['country'].str.contains("United Kingdom"))
                   & (df['rating'].str.contains('PG'))]
    print(df_movies.sample(3))


# 10 самых длинных фильмов
def get_longest_movies(df):
    df_movies = df[(df['type'] == 'Movie')]
    df_movies['duration'] = df_movies['duration'].str.split(' ', expand=True)
    df_movies['duration'] = pd.to_numeric(df_movies['duration'])
    df_movies = df_movies.sort_values(by='duration', ascending=False)
    res = pd.Series(df_movies.duration.values, index=df_movies.title).to_dict()
    res = dict(islice(res.items(), 10))
    for key in res.keys():
        print(key + ': ' + str(res[key]) + ' minutes')


# 10 случайных фильмов
def get_ten_random_movies(df):
    df_movies = df[(df['type'] == 'Movie')]
    res = df_movies.sample(10)[['title', 'description']]
    res = pd.Series(res.description.values, index=res.title).to_dict()
    for key in res.keys():
        print(f'Title: {key}\n'
              f'Description: {res[key]}\n'
              f'-----------------------------------------------------------------------------\n')

# Расскомментируйте вызовы функций для их теста
#get_ten_random_movies(df)
#get_random_pg(df)
#get_longest_running_shows(df)
#get_longest_movies(df)