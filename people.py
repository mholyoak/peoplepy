

class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def GetFirstName(self):
        return self.first

    def GetLastName(self):
        return self.last

    def GetAge(self):
        return self.age


print("Hello People")

people = []
people.append(Person("John", "Doe", 10))
people.append(Person("Sue", "Kitchens", 15))

for person in people:
    print("Person: {} {} {}".format(person.GetFirstName(), person.GetLastName(), person.GetAge()))

print("Finished")