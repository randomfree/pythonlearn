name = 'Swaroop'

if name.startswith('Swa'):
    print('yes, the string starts with "Swa"')

if 'a' in name:
    print('yes , it contains the string "a"')

if name.find('war')!=-1:
    print('yes,it contains the string "war"')

delimiter='_*_'
mylist=['Brazil','Russia','India','china']
print(delimiter.join(mylist))
