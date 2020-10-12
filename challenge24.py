# challenge 24

users = {}


class library:
    def __init__(self, listofbooks, library_name):
        self.list = listofbooks
        self.name = library_name

    def display_book(self):
        print("\nThe books in the library are : ")
        flag = 0
        for book in self.list:
            if self.list[book] > 0:
                print(" ", book)
                flag = 1
        if flag == 0:
            print("\nThe Library is empty :( ")

    def add_book(self):
        book = input("\nEnter book to be borrowed : ").lower()
        if book in self.list:
            if self.list[book] > 0:
                user = input("\nEnter your name : ").lower()
                self.list[book] -= 1
                users[book] = user
            else:
                print(
                    "\nThe book is not avalaible, its already borrowed by ", users[book])
        else:
            print("\nThis book is not avalaible in the library")

    def lend_book(self):
        book = input("\nEnter book to be lent : ").lower()
        if book in self.list:
            self.list[book] += 1
        else:
            self.list[book] = 1

    def return_book(self):
        book = input("\nEnter book to be returned : ").lower()
        if book in self.list:
            self.list[book] += 1
        else:
            print("\nThat book does not belong to this library")


def main():
    list = {}  # book : quantity
    lib_name = 'Pustakalay'
    lib = library(list, lib_name)

    exit = 0

    while not exit:
        c = int(input("\n\n Enter Choice :\n 1.Display Book \n 2.Add Book (borrow from library) \n 3.Lend Book \n 4.Return Book \n 5.Exit \n\n"))

        if c == 1:
            lib.display_book()
        elif c == 2:
            lib.add_book()
        elif c == 3:
            lib.lend_book()
        elif c == 4:
            lib.return_book()
        elif c == 5:
            exit = 1
        else:
            print("\n Wrong Input!!!")


if __name__ == "__main__":
    main()
