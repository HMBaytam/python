'''
This excersice is just to get used to the difference between a class and an object
And when to use the is-a and has-a terms
'''

# Animal is-a object (yes, sort of confusing) look ar the extra credit


class Animal(object):
    pass

# Dog is-a Animal (getting a bit more confusing)


class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat is-a Animal


class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-a object


class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is-a Person


class Employee(Person):

    def __init__(self, name, salary):
        # inherits name from Person and sets it to the name in params
        super(Employee, self).__init__(name)

        # Employee has-a salary
        self.salary = salary
# Fish is-a object


class Fish(object):
    pass

# Salmon is-a Fish


class Salmon(Fish):
    pass

# Halibut is-a Fish


class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog('Rover')

# satan is-a Cat
satan = Cat('Satan')

# mary is-a person
mary = Person('Mary')

# mary has-a pet named satan
mary.pet = satan


# frank is-a Employee
frank = Employee('Frank', 120000)

# frank has a pet named rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
