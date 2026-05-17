#inheritance 

class Song():
    def __init__(self,title):
        self.title=title

    def play(self):
        print("Playing..",self.title)

class PopSong(Song):
    def dance(self):
        print("Dancing on",self.title)

song1=PopSong("Runaway")
song1.play()#inherited method
song1.dance()#its own method