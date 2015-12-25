class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)

    def lastName(self):
        return self.name.split()[-1];

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


