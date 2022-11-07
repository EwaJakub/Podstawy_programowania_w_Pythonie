from datetime import date

name = input('Podaj swoje imię:')
birth_year = int(input('Podaj rok swojego urodzenia:'))
age = date.today().year - birth_year

print(f'Użytkownik: {name} jest w wieku {age} lat.')
