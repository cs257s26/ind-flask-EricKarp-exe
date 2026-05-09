DROP TABLE IF EXISTS stolen_art;
CREATE TABLE stolen_art (
    artwork VARCHAR(30),
    artist VARCHAR(30),
    medium VARCHAR(30),
);

DROP TABLE IF EXISTS artist_origin;
CREATE TABLE artist_origin (
    artist VARCHAR(30),
    origin VARCHAR(30),
    link TEXT,
)