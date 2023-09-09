class person: 
    name = "sarah"
    age = 17

    def is_adult(self):
        if self.age >= 18:
            print("You have too much responsibilities")
        elif self.age < 18 :
            print("lucky")
        else:
            print("babyyyy")    

    def __str__(self):
        return f"this person is called {self.name} and is {self.age} years old"

first_person = person()
print(first_person.name)
print(first_person.age)

first_person.is_adult()

class person:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def __str__(self):
        return f"my {self.name} and i am {self.age} years"
    
person = person("john", 22)
print(person)
