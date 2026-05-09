# README

Individual Flask project using a SQL database.

I used the same data and in the same structure that the team used in our csv files as the code and tests were already built around them being in that format. I represented this through two tables, one being the stolen artwork taken from the interpo_classified_stolen..etc csv file and the other being the origins of various artists. For the artist_origin datatable I used artist, origin, and the link to the image of the artist. For the stolen_art datatable I used the artwork name, the artist's anme, and the medium of their work.

The user stories represented are the same as they were before. sql_origin_count represents a user who is curious to see what country has had the most artists with stolen artwork. sql_find_artwork represents a user who is curious about what artworks a particular artist has had stolen from them.