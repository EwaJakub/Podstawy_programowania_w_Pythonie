![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 &ndash; Pętla `while`

W pliku `task.py` wypisz na ekran 10 razy: `Jestem programistą Pythona` lub `Jestem programistką Pythona` (wybierz jedno).

> Użyj pętli while.


## Zadanie 2 &ndash; Kolejne potęgi

W pliku `task.py` napisz program, który obliczy kolejne potęgi liczby 2 dla wykładnika z przedziału od 0 do 10 włącznie.

Wyświetl wynik w postaci:
```
2 do potęgi 0 to 1
2 do potęgi 1 to 2
2 do potęgi 2 to 4
2 do potęgi 3 to 8
2 do potęgi 4 to 16
2 do potęgi 5 to 32
2 do potęgi 6 to 64
2 do potęgi 7 to 128
2 do potęgi 8 to 256
2 do potęgi 9 to 512
2 do potęgi 10 to 1024
```

> Użyj pętli `for`.


## Zadanie 3 &ndash; Porównanie imion

W pliku `task.py` napisz program, który:

* wyświetli na ekranie komunikat `Podaj pierwsze imię: `,
* pobierze z klawiatury imię i zapisze go do zmiennej `first_name`,
* wyświetli na ekranie komunikat `Podaj drugie imię: `,
* pobierze z klawiatury drugie imię użytkownika i zapisze go do zmiennej `second_name`,
* wyświetli na ekranie `Takie same` jeżeli imiona są takie same albo `Różne` jeżeli są różne.

> Podpowiedź: użyj instrukcji warunkowej `if`!


## Zadanie 4 &ndash; Porównanie liczb

W pliku `task.py` napisz program, który przyjmie od użytkownika liczby `a` i `b`.

Wypisz informację która z nich jest większa w postaci:
```
a jest większe!
```
lub
```
b jest większe!
```

> Podpowiedź: pamiętaj o rzutowaniu liczb na typ liczbowy (np. `float`)!
> Stringi porównywane są z zachowaniem porządku leksykograficznego.


## Zadanie 5 &ndash; Równania kwadratowe

W pliku `task.py` napisz program, który pomoże licealistom w liczeniu pierwiastków równań kwadratowych. Program ma:

* wyświetlić na ekranie komunikat: `Równanie w postaci a*x**2 + b*x + c == 0`,
* wyświetlić na ekranie komunikat: `Podaj a`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `a` (pamiętaj o rzutowaniu na odpowiedni typ),
* wyświetlić na ekranie komunikat: `Podaj b`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `b` (pamiętaj o rzutowaniu na odpowiedni typ),
* wyświetlić na ekranie komunikat: `Podaj c`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `c` (pamiętaj o rzutowaniu na odpowiedni typ),
* policzy deltę,
* jeśli delta > 0, policzyć wartości `x_1` i `x_2` ze wzoru:
```
x_1 = (-b - delta**0.5) / (2 * a)
x_2 = (-b + delta**0.5) / (2 * a)
```
a następnie wyświetlić je w postaci:
```
Pierwiastki równania kwadratowego:
x_1 = <wartość>
x_2 = <wartość>
```
* jeżeli delta = 0, policzyć wartości `x_1` i `x_2` a następnie wyświetlić ją na ekranie w postaci:
```
Pierwiastki równania kwadratowego:
x_1 = x_2 = <wartość>

```
* jeżeli delta jest ujemna, wypisz na ekran `brak rozwiązań`.

**Uwaga** Zakładamy, że użytkownik poprawnie poda liczby `a`, `b` i `c`.


## Zadanie 6 &ndash; Suma liczb

W pliku `task.py` napisz program, który policzy sumę wszystkich liczb od 0 do `n`, gdzie `n` jest podane przez użytkownika.

Przykład:
```
Podaj n: 4
10
```


## Zadanie 7 &ndash; Średnia

W pliku `task.py` napisz program, który:
* stworzy zmienną `numbers` i przypisze do niej pustą listę,
* przyjmie od użytkownika informację, ile liczb ten chce wprowadzić i zapamięta tą informację w zmiennej `n`,
* w pętli (która wykona się `n` razy):
  * zapyta użytkownika o liczbę
  * dopisze podaną przez użytkownika liczbę na koniec listy `numbers`
* policzy ich sumę i średnią,
* wypisze na ekran te liczby oraz informację czy suma jest większa od średniej:
```
Podaj n: 4
Podaj liczbę: 1
Podaj liczbę: 2
Podaj liczbę: -4
Podaj liczbę: 5
Wprowadzone liczby: 1 2 -4 5
Suma: 4,
Średnia: 1
Suma jest większa!
```


## Zadanie 8 &ndash; Definiowanie listy liczb

* Zdefiniuj listę składającą się z liczb od 1 do 8.
* Wypisz każdą z tych liczb w osobnym wierszu, poprzedzoną słowem `liczba: `.

Przykład:
```
liczba: 1
liczba: 2
liczba: 3
liczba: 4
liczba: 5
liczba: 6
liczba: 7
liczba: 8
```


## Zadanie 9 &ndash; Tabliczka mnożenia

W pliku `task.py` napisz program, który pobierze od użytkownika liczbę `n` (z przedziału od 1 do 10), a następnie wygeneruje działania z wynikami mnożenia podanego `n` przez liczby od 1 do 10.

##### Oczekiwany wynik:
```
Podaj liczbę: 3
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
6 * 3 = 18
7 * 3 = 21
8 * 3 = 24
9 * 3 = 27
10 * 3 = 30
```


## Zadanie 10 &ndash; Fizzbuzz

W pliku `task.py` użyj pętli `for` aby napisać program FizzBuzz. W pętli, która wykona się dla liczb z zakresu od 1 do 100 (włącznie):
* jeżeli liczba jest podzielna przez 3 i 5, wypisz na ekranie `FizzBuzz` (przykładowo dla liczby 15 ma się wypisać **tylko** `FizzBuzz`),
* jeżeli liczba jest podzielna przez 3, wypisz na ekran `Fizz`,
* jeżeli liczba jest podzielna przez 5, wypisz na ekran `Buzz`,
* w przeciwnym wypadku wypisz na ekran liczbę.

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
...
```
