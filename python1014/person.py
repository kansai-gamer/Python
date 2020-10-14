class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name}.")
        print(f"My age is {self.age}.")

class Student(Person):
    def __init__(self, name, age, school_name):
        super().__init__(name, age)
        self.school_name = school_name

    def study(self):
        print(f"{self.name} studies programing.")

    def greet(self):
        super().greet()
        print(f"My school is {self.school_name}.")


person = Student("kansai", 20, "osaka-pg")
person.greet()
person.study()