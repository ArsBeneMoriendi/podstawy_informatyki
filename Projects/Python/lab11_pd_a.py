class MyMusicClass:
    def __init__(self, artist, year, most_popular, listeners):
        self.artist = artist
        self.year = year
        self.most_popular = most_popular
        self.listeners = listeners


musicList = []
n = 0

try:
    for i in range(7):
        n += 1
        print(f"\nPosition number {n}.")
        musicList.append(MyMusicClass(input("Artist's name: "),
                                      int(input("Creation or debut year: ")),
                                      input("Most popular song on Spotify: "),
                                      int(input("Number of listeners: "))))
except ValueError:
    print(f"\nYou've entered an unacceptable value at position number {n}.")
