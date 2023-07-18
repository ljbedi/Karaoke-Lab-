class Room:

    def __init__(self, number):
        self.number = number 
        self.guest_list = []
        self.songs = []

        # self.availability = availability 
        # self.songs = songs

    def number_of_guests(self):
        return len(self.guest_list)
    
    def number_of_songs(self):
        return len(self.songs)

    def check_in_guest(self, guest):
        self.guest_list.append(guest)

    def check_out_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, songs):
        self.songs.append(songs)


    