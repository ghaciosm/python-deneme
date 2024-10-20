person = {
    'isim': 'gulcin',
    'soy_isim': 'haci',
    'yas': 21
}

# person = dict(isim= 'gulcin', soy_isim= 'haci', yas= 21) 

person_2 = {
    'isim': 'musab',
    'soy_isim': 'kardes',
    'yas': 22
}

person['color'] = 'red'

# print(person_2.get('yas', False))

# print(person['soy_isim'])
# print(person)

# for anahtar, deger in person.items():
#     print(anahtar, "=", deger)

# for key in person_2.keys():
#     print(person[key])

for value in person.values():
    print(value)

