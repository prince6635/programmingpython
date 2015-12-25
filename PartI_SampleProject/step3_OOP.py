from step3_lib.person import Person
from step3_lib.manager import Manager
from step3_lib.make_db_classes import loadDbase, storeDbase, updateDbase

print("test Person class")
bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
print(bob.name, sue.pay)

print(bob.lastName())
sue.giveRaise(.10)
print(sue.pay)
print("==================")

print("test Manager class")
tom = Manager(name='Tom Doe', age=50, pay=50000)
print(tom.lastName())
tom.giveRaise(.20)
print(tom.pay)
print(tom) # __str__
print("==================")

print("test persisting in shelve db")
storeDbase()
loadDbase()

updateDbase()
loadDbase()
print("==================")



