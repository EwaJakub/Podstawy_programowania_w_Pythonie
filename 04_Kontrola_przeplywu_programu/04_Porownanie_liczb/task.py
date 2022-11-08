a = float(input('Podaj pierwszą liczbę:'))
b = float(input('Podaj drugą liczbę:'))

if a > b:
    print(f'a = {a} jest większe!')
elif a < b:
    print(f'b = {b} jest większe!')
else:
    print(f'a = {a} i b = {b} są równe!')
