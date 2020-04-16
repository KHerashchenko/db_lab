CREATE TABLE Genres
(
genre_id integer,
name char(20)
);

ALTER TABLE Genres
ADD CONSTRAINT genre_pk PRIMARY KEY (genre_id);

-- 

CREATE TABLE Artists
(
artist_id integer,
name char(20)
);

ALTER TABLE Artists
ADD CONSTRAINT artist_pk PRIMARY KEY (artist_id);

-- 

CREATE TABLE Songs
(
song_id integer,
title char(20),
genre_id integer,
beats_per_min integer,
energy integer,
danceability integer,
loudness integer,
liveness integer,
valence integer,
length integer,
cousticness integer,
speechiness integer
);

ALTER TABLE Songs
ADD CONSTRAINT song_pk 
    PRIMARY KEY (song_id);
  
ALTER TABLE Songs
ADD CONSTRAINT song_genre_pk
  FOREIGN KEY (genre_id)
  REFERENCES Genres (genre_id);
  
-- 

CREATE TABLE SongsArtists
(
artist_id integer,
song_id integer
);

ALTER TABLE SongsArtists
ADD CONSTRAINT song_artist_pk PRIMARY KEY (artist_id, song_id);
