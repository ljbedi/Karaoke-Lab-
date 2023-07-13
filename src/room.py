from songs import Songs

class Room:

    def __init__(self, number):
        self.number = number 
        self.guest_list = []

        # self.availability = availability 
        # self.songs = songs

    def add_guest(self, guest):
        self.guest_list.append(guest)