import unittest

from src.room import Room 
from src.guest import Guest 
from src.songs import Songs

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("1")
        self.room_2 = Room("2")
        self.room_3 = Room("3")
        self.guest_1 = Guest("Liam Bailey")
        self.guest_2 = Guest("Holly Tyler")
        self.guest_3 = Guest("Brandon Noone")
        self.guest_list = [self.guest_1, self.guest_2]
        self.song_1 = Songs("Cuff It")
        self.song_2 = Songs("Heated")
        self.songs = [self.song_1, self.song_2]

    # def add_a_song_to_room(self, guest, room):
    #     self.room_1 = Room("Room 1", 50, self.song_1) 

    def test_room_has_no_guests_at_start(self):
        self.assertEqual(0, self.room_1.number_of_guests())

    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room_1.number_of_guests())

    def test_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room_1.number_of_guests())

    def test_add_song(self):
        Songs = ("Cuff It")
        self.room_2.add_song(self.songs)
        self.assertEqual(1, self.room_2.number_of_songs())







    # def does_room_have_space(self):
    #     self.room_1 = Room("Room 1", 10, 0)
    #     if  self.room_1.availability <= 10
    #         return "Have fun!!"
    #     elif:
    #         return "The room is full!"
        

        