import cx_Oracle
import pandas as pd

username = 'system'
password = 'orcl'

connection = cx_Oracle.connect(username, password)

cursor = connection.cursor()


def execute_query_via_pd(query):
    SQL_Query = pd.read_sql_query(query, connection)
    return SQL_Query

def execute_query_via_cur(query):
    cursor.execute(query)
    cursor.execute(query)
    data = pd.DataFrame(cursor.fetchall())
    return data


query1 = '''
select count(*) as num_of_songs, trim(Genres.name) as genre_name
from Songs
    join Genres
    on Genres.genre_id = Songs.genre_id
group by Genres.name
'''
print(query1)
data = execute_query_via_pd(query1)
print(data)

# data = execute_query_via_cur(query1)
# data.columns = ['NUM_OF_SONGS', 'GENRE_NAME']
# print(data)


query2 = '''
select trim(Artists.name) as artist_name,
    round( count(SongsArtists.song_id)*100/(select count(*) from SongsArtists), 2) as songs_percentile
from SongsArtists
    join Artists
    on SongsArtists.artist_id = Artists.artist_id
    join Songs
    on Songs.song_id = SongsArtists.song_id
group by Artists.name
'''
print(query2)
data = execute_query_via_pd(query2)
print(data)

# data = execute_query_via_cur(query2)
# data.columns = ['NUM_OF_SONGS', 'GENRE_NAME']
# print(data)


query3 = '''
 select loudness, round(avg(popularity),2) as popularity
 from Songs
 group by loudness
'''
print(query3)
data = execute_query_via_pd(query3)
print(data)

# data = execute_query_via_cur(query3)
# data.columns = ['NUM_OF_SONGS', 'GENRE_NAME']
# print(data)

cursor.close()

connection.close()
