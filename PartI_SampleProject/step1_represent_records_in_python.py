# 1, use Lists
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
print(bob[0], sue[2])
print(bob[0].split()[-1]) # bob's last name
sue[2] *= 1.25 # give sue a 25% raise
print(sue)

# 2, use a list of lists
people = [bob, sue]
for person in people:
    print(person)

print people[1][0]
for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.25
    print(person[2])

# 3, Python's powerful iteration tools
#   3.1, list comprehensions
pays = [person[2] for person in people]
print(pays)

#   3.2, maps
pays = map((lambda x: x[2]), people)
print(list(pays))

#   3.3, generator expression
print(sum(person[2] for person in people))

# 4, Add a record
people.append(['Tom', 50, 0, None])
print(len(people))

# 5, use field labels
NAME, AGE, PAY = range(3)
print(bob[NAME])

# 6, use Dictionaries (3 ways to create a dictionary)
gary = {'name': 'Gary Brown', 'age': 42, 'pay': 80000, 'job': 'dev'}

# betty = {'name': 'Betty Lee', 'age': 39, 'pay': 76000, 'job': 'design'}
betty = dict(name='Betty Lee', age=39, pay=70000, job='design')

paul_names = ['name', 'age', 'pay', 'job']
paul_values = ['Paul Holden', 45, 50000, 'manager']
paul = dict(zip(paul_names, paul_values))

print(gary['name'].split()[-1])
betty['pay'] *= 1.25
print(betty['pay'])
print(paul)
people = [gary, betty, paul]
for person in people:
    if person['name'] == 'Paul Holden':
        print(person)

#   6.1, iteration tools
names = [person['name'] for person in people]
print(names)
names = list(map((lambda x: x['name']), people))
print(names)
print(sum(person['pay'] for person in people))

#   6.2, SQL-ish query
result = [person['name'] for person in people if person['age'] >= 45]
print(result)
result = [(person['age'] * 2 if person['age'] >= 45 else person['age']) for person in people]
print(result)

#   6.3, dictionay of dictionaries
db = {}
db['bob'] = bob
db['sue'] = sue
for key in db:
    print(key, '=>', db[key])

# 7, nested structure
bob2 = {
    'name': {'first': 'Bob', 'last': 'Smith'},
    'age': 42,
    'job': ['software', 'writing'],
    'pay': (40000, 50000)
}
















