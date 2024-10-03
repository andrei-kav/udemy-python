from datetime import datetime


class Dog:
    def bark(self):
        print(f'{self.name} is barking')

    def age(self):
        age = datetime.today().year - self.born
        print(f'{self.name} is {age} year(s) old')

my_pup = Dog()
my_pup.name = 'Beautiful'
my_pup.born = 2011
my_pup.bark()
my_pup.age()

another_pup = Dog()
another_pup.name = 'Another Beautiful'
another_pup.born = 2023
another_pup.bark()
another_pup.age()