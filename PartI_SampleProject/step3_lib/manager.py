# Inheritance

from person import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus=0.1):
        # self.pay *= (1.0 + percent + bonus)
        # refactor: instance.method(arg1, arg2) and class.method(instance, arg1, arg2) are the same
        Person.giveRaise(self, percent + bonus)

