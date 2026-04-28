from app import app
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get("/", follow_redirects = True)
        self.assertEqual(200, response.status_code)
        self.assertEqual(b'<p> /country_origin/ <p> \n <p> /artist_name/ <p>', response.data)
    
    def test_web_origin_count(self):
        self.assertEqual(self.app.get("/country_origin/France").data, b"The number of artists with stolen art who are from France: 10")
        self.assertEqual(self.app.get("/country_origin/Mexico").data, b'The number of artists with stolen art who are from Mexico: 1')
        self.assertEqual(self.app.get("/country_origin/asdfasdfadf").status_code, 500)
    
    def test_web_find_artwork(self):
        self.assertEqual(self.app.get("/artist_name/Gustav%20Klimt").data, b'4')
        self.assertEqual(self.app.get("/artist_name/Andy%20Warhol").data, b'40')
        self.assertEqual(self.app.get("/artist_name/Theodore%20Roosevelt").data, b'0')