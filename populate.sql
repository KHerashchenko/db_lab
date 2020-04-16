INSERT INTO Artists(artist_id, name)
VALUES(1, 'Alex Clare');
INSERT INTO Artists(artist_id, name)
VALUES(2, 'Two feet');
INSERT INTO Artists(artist_id, name)
VALUES(3, 'aiwake');

INSERT INTO Genres(genre_id, name)
VALUES(1, 'pop');
INSERT INTO Genres(genre_id, name)
VALUES(2, 'rock');
INSERT INTO Genres(genre_id, name)
VALUES(3, 'indian pop');

INSERT INTO Songs(song_id,title,artist_id,genre_id,beats_per_min,energy,danceability,loudness,liveness,valence,length,acousticness,speechiness,popularity)
VALUES(1,'Childish',3,50,67,65,34,36,90,445,32,17,98);
INSERT INTO Songs(song_id,title,artist_id,genre_id,beats_per_min,energy,danceability,loudness,liveness,valence,length,acousticness,speechiness,popularity)
VALUES(2,'Palm City',2,54,57,75,65,32,90,235,23,11,77);
INSERT INTO Songs(song_id,title,artist_id,genre_id,beats_per_min,energy,danceability,loudness,liveness,valence,length,acousticness,speechiness,popularity)
VALUES(3,'a lot',2,0,37,634,35,32,33,445,43,37,65);
INSERT INTO Songs(song_id,title,artist_id,genre_id,beats_per_min,energy,danceability,loudness,liveness,valence,length,acousticness,speechiness,popularity)
VALUES(4,'Rockstar',1,54,27,23,34,45,90,345,352,45,90);
INSERT INTO Songs(song_id,title,artist_id,genre_id,beats_per_min,energy,danceability,loudness,liveness,valence,length,acousticness,speechiness,popularity)
VALUES(5,'Birds',2,50,13,34,24,35,455,56,19,57);

INSERT INTO SongsArtists(artist_id, song_id)
VALUES(3, 3);
INSERT INTO SongsArtists(artist_id, song_id)
VALUES(1, 2);
INSERT INTO SongsArtists(artist_id, song_id)
VALUES(2, 5);
INSERT INTO SongsArtists(artist_id, song_id)
VALUES(1, 5);
INSERT INTO SongsArtists(artist_id, song_id)
VALUES(2, 4);
INSERT INTO SongsArtists(artist_id, song_id)
VALUES(3, 1);
