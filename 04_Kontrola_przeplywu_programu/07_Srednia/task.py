numbers = []
n = int(input('Podaj n: '))

for i in range(n):
    number = int(input('Podaj liczbę: '))
    numbers.append(number)

summary = sum(numbers)
average = summary / len(numbers)

print(f'Wprowadzone liczby: {numbers}')
print(f'Suma: {summary}')
print(f'Średnia: {average}')
if summary > average:
    print('Suma jest większa!')
elif summary < average:
    print('Średnia jest większa!')
else:
    print('Suma i średnia są równe!')
