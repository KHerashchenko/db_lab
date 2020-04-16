-- task1
select count(*) as num_of_songs, Genres.name as genre_name
from Songs
    join Genres
    on Genres.genre_id = Songs.genre_id
group by Genres.name;

-- task2

select Artists.name, 
    round( count(SongsArtists.song_id)*100/(select count(*) from SongsArtists), 2) as songs_percentile
from SongsArtists
    join Artists
    on SongsArtists.artist_id = Artists.artist_id
    join Songs
    on Songs.song_id = SongsArtists.song_id
group by Artists.name;

-- task3

 select loudness, round(avg(popularity),2)
 from Songs
 group by loudness;
