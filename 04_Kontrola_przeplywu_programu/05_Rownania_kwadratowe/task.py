print('Równanie w postaci a*x**2 + b*x + c == 0')
a = float(input('Podaj a '))
b = float(input('Podaj b '))
c = float(input('Podaj c '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x_1 = (-b - delta ** 0.5) / (2 * a)
    x_2 = (-b + delta ** 0.5) / (2 * a)
    print(f'Pierwiastki równania kwadratowego: \n x_1 = {x_1} \n x_2 = {x_2}')
elif delta == 0:
    x_1 = (-b - delta ** 0.5) / (2 * a)
    x_2 = (-b + delta ** 0.5) / (2 * a)
    print(f'Pierwiastki równania kwadratowego: x_1 = x_2 = {x_1}')
else:
    print('Brak rozwiązań')
