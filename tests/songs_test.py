import unittest

from src.songs import Songs

class TestSongs(unittest.TestCase):
    
    def setUp(self):
        self.songs = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5, self.song_6]
        self.song_1 = Songs("Cuff It")
        self.song_2 = Songs("Heated")
        self.song_3 = Songs("Alien Superstar")
        self.song_4 = Songs("Move")
        self.song_5 = Songs("Pure/Honey")
        self.song_6 = Songs("My Power")

    
