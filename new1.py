# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         if hasattr(self, 'name'):
#             return self.name,self.age
#         return self.age
#
#
#
# person1 = Person("Ali", 25)
# person2 = Person("Vali", 29)
# person3 = Person("Lali", 21)
#
# del person1.name
# print(person1.get_info())





#
# class MyClass:
#
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#
#     def __getattr__(self, item):
#         return f"{item} obj da mavjud emas"
#
#     def __getattribute__(self, item):
#         if hasattr(item):
#             return super().__getattribute__(item)
#         return None
#
#
# m = MyClass('study', 12)
# m.count = 101
# print(m.count)




# class MyClass:
#
#     def __delattr__(self, name):
#
#         print(f"Atribut o‘chirilmoqda: {name}")
#
#         super().__delattr__(name)
#
#
# obj = MyClass()
#
# obj.x = 10
#
# del obj.x  # "Atribut o‘chirilmoqda: x"















#
# class Animal:
#     def __init__(self, name):
#         self.name=name
#     def speak(self):
#         return "Nomalum ovoz"
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Vov-vov"
#
# dog = Dog("Rex")
# print(dog.name)
# print(dog.speak())















# Library title,genre,location
# cataolog,book,magazine,audiobook,display
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    count=0
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        LibraryItem.count+=1

    @abstractmethod
    def locate(self):
        pass

    @classmethod
    def count_get(cls):
        return cls.count


class Book(LibraryItem):
    def __init__(self, title, genre, isbn, authors):
        super().__init__(title, genre)
        self.isbn = isbn
        self.authors = authors

    def locate(self):
        return f"Kitoblar bo'limida joy olgan"


    def __str__(self):
        return  f"{self.title}"

class Magazine(LibraryItem):
    def __init__(self, title, genre,volume):
        super().__init__(title, genre)
        self.volume = volume

    def locate(self):
        return f"Jurnallar bo'limida joy olgan"

class Audiobook(LibraryItem):
    def __init__(self, title, genre, time):
        super().__init__(title, genre)
        self.time = time


    def locate(self):
        return f"Audio bo'limida joy olgan"

class DisplayBook(LibraryItem):
    def __init__(self, title, genre, type_dvd):
        super().__init__(title, genre)
        self.type_dvd = type_dvd

    def locate(self):
        return f"Displaylar bo'limida joy olgan"


class Catalog:
    def __init__(self):
        self.books = []


    def add(self, item):
        self.books.append(item)

def brain_stop():
    cat = Catalog()
    print("""
    1 Add book
    2 Add magazine
    3 Add audiobook
    4 Add displaybook
    5 exit
    """)
    while True:
        nums=input("Enter your choice: ")

        while True:

            if nums == "1":
                title = input("Enter title: ")
                genre = input("Enter genre: ")
                isbn=input("Enter ISBN: ")
                authors=input("Enter authors: ")
                item=Book(title, genre, isbn, authors)
                print(item.locate())
                cat.add(item)
            elif nums == "2":
                title = input("Enter title: ")
                genre = input("Enter genre: ")
                volume=input("Enter Volume: ")
                item=Magazine(title, genre, volume)
                print(item.locate())
                cat.add(item)
            elif nums == "3":
                title = input("Enter title: ")
                genre = input("Enter genre: ")
                time=input("Enter Time: ")
                item=Audiobook(title, genre, time)
                print(item.locate())
                cat.add(item)
            elif nums == "4":
                title = input("Enter title: ")
                genre = input("Enter genre: ")
                type_dvd=input("Enter Type_dvd: ")
                item=DisplayBook(title, genre, type_dvd)
                print(item.locate())
                cat.add(item)
                print(cat.books)

brain_stop()









