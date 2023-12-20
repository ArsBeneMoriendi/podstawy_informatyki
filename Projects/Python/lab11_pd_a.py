class MyMusicClass:
    def __init__(self, artist, year, most_popular, listeners):
        self.artist = artist
        self.year = year
        self.most_popular = most_popular
        self.listeners = listeners


list1 = []
i = 0


try:
    for i in range(7):
        i += 1
        print(f"\nPosition number {i}.")
        list1.append(MyMusicClass(input("Artist's name: "),
                                  int(input("Creation or debut year: ")),
                                  input("Most popular song on Spotify: "),
                                  int(input("Number of listeners: "))))
except ValueError:
    print(f"\nYou've entered an unacceptable value at position number {i}.")
