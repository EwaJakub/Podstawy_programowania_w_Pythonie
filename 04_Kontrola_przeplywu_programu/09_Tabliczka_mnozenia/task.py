n = 0
while n < 1 or n > 10:
    n = int(input('Podaj n od 1 do 10: '))

for element in range(1, 11):
    print(f'{element} * {n} = {element * n}')
