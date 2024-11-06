#Работа со словарями:
my_dict = {'Matvey': 2004, 'Kir': 2003, 'Kriko': 2006, 'Igor': 2009 }
print(my_dict)
print(my_dict['Matvey'])
my_dict.update({'Grisha': 1982,
                 'Anna': 1983})
print(my_dict)
del my_dict['Kriko']
print(my_dict.get('Kriko'))

#Работа со множествами:
my_set = {1,2,3,2,1,1, 'book', 'string', 'book', True,}
print(my_set)
my_set.update(["cake",(1,2,3)])
my_set.discard(2)
print(my_set)
