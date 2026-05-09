DROP TABLE IF EXISTS stolen_art;
CREATE TABLE stolen_art (
    artwork VARCHAR(50),
    artist VARCHAR(50),
    medium VARCHAR(50)
);

DROP TABLE IF EXISTS artist_origin;
CREATE TABLE artist_origin (
    artist VARCHAR(50),
    origin VARCHAR(50),
    link TEXT
);