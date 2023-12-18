# class MySeriesClass:
#    serial = "The 100"


# S1 = MySeriesClass()
# print(S1.serial)


class MySeriesRankClass:
    def __init__(self, title, director, idbm):
        self.title = title
        self.director = director
        self.idbm = idbm


def movie():
    o1 = MySeriesRankClass(input("\nEnter a title: "), input("Who is the director: "), input("Enter the IDBM rank: "))
    print(f"\nTitle: {o1.title}\nDirector: {o1.director}\nIDBM rank: {o1.idbm}")


def question():
    quest = input("\nDo you want to enter the next movie? (Y/N)\n")
    if quest.upper() == "Y":
        movie()
        question()


movie()
question()

