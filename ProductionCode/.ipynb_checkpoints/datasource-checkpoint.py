import psycopg2
from ProductionCode.psqlConfig import *

def sql_find_creator(name_of_artwork):
    """Returns who created the given piece of artwork

    Args:
        name_of_artwork (str): the name of the artwork
    
    Returns:
        string or None: the name of the creator if the artwork is in the database,
            otherwise None"""
    # Checks if the type of input is correct
    if (type(name_of_artwork) != str):
         raise TypeError("please provide a valid input")

    with psycopg2.connect(f"dbname='{database_name}' user='{username}' password='{db_password}'") as conn:
        cur = conn.cursor()
    
        cur.execute(f"SELECT artist FROM stolen_art WHERE artwork = '{name_of_artwork}'")
        
        tbr = str(cur.fetchone()[0])
    
        cur.close()

        return tbr if tbr != "" else None

def sql_find_artwork(name_of_creator):
    """Returns all artworks by the given creator

    Args:
        name_of_creator (str): the name of the creator
    
    Returns:
        list[str]: a list of artwork names by the creator (empty if none found)"""
    # Checks if the type of input is correct
    if (type(name_of_artwork) != str):
         raise TypeError("please provide a valid input")

    with psycopg2.connect(f"dbname='{database_name}' user='{username}' password='{db_password}'") as conn:
        cur = conn.cursor()
    
        cur.execute(f"SELECT artwork FROM stolen_art WHERE artist = '{name_of_creator}'")

        tbr = [artwork[0] for artwork in cur.fetchall()]
    
        cur.close()

        return tbr if tbr != [] else None

def sql_origin_count(origin):
    """Returns the number of artist in total from given orgin by checking the sql database

    Args:
        orgin (str): the country of artist's orgin 
    
    Returns:
        string or None: the count of artists from that orgin if in our database,
            otherwise None"""
    
    # Checks if the type of input is correct
    if (type(origin) != str):
        raise TypeError("Please provide a valid input.")

    with psycopg2.connect(f"dbname='{database_name}' user='{username}' password='{db_password}'") as conn:
        cur = conn.cursor()
    
        cur.execute(f"SELECT artist FROM artist_origin WHERE origin = '{origin}'")
        origin_count = len(cur.fetchall())
    
        cur.close()

    if(origin_count == 0):
        return None
    else:
        return("The number of artists with stolen art who are from " + origin + ": " + str(origin_count))


def sql_count_stolen_by_artist(name_of_creator):
    """Returns the number of stolen artwork by a given artist by checking the sql database

    Args:
        artist (str): the artist whom you want stolen works count 
    
    Returns:
        int: the count of stolen works by a given artist"""
    
    # Checks if the type of input is correct
    if not isinstance(name_of_creator, str):
         raise TypeError("please provide a valid input")

    with psycopg2.connect(f"dbname='{database_name}' user='{username}' password='{db_password}'") as conn:
        cur = conn.cursor()
    
        cur.execute(f"SELECT artwork FROM stolen_art WHERE artist = '{name_of_creator}'")
        stolen_count = len(cur.fetchall())
    
        cur.close()

    return str(stolen_count)