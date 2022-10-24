![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 &ndash; Pobieranie danych od użytkownika.

W pliku `task.py` napisz program, który:

1. pobierze z klawiatury imię użytkownika,
2. pobierze z klawiatury nazwisko użytkownika,
3. wyświetli komunikat "Imię Nazwisko jest programistą Pythona!"

**Przykład:**
```
Podaj imię: Guido
Podaj nazwisko: van Rossum
Guido van Rossum jest programistą Pythona!
```

**Podpowiedź:** zapisuj wpisywane przez użytkownika dane do zmiennych.


## Zadanie 2 &ndash; Łączenie listy

W pliku `task.py` zdefiniuj listę `letters` składającą się z liter od `a` do `e`. Następnie wypisz te litery połączone znakiem spacji.

Do połączenia liter ze sobą użyj metody `join`.

Wynikiem działania Twojego programu powinno być:
```
a b c d e
```


## Zadanie 3 &ndash; Dzielenie modulo

W pliku `task.py` stwórz zmienne o nazwach `a` oraz `b` i przypisz do nich dowolne liczby. Oblicz resztę z dzielenia (modulo) tych liczb i przypisz wynik do zmiennej `result`.

Wypisz zmienną `result` w konsoli.

> Jeżeli nie do końca rozumiesz działanie operatora modulo przećwicz to z innymi liczbami.

Przykładowy wynik działania programu (dla `a = 53` oraz `b = 17`):
```
2
```


## Zadanie 4 &ndash; inkrementacja i dekrementacja

W pliku `task.py` znajdziesz zmienną `counter` o wartości `145`. Następnie:
* wypisz jej wartość w konsoli
* za pomocą inkrementacji o 1 zwiększ wartość zmiennej `counter`,
* wypisz ją w konsoli,
* za pomocą dekrementacji o 1 zmniejsz wartość zmiennej `counter`,
* wypisz ją w konsoli.

###### Użyj zapisu skróconego!


## Zadanie 5 &ndash; Porównywanie zmiennych

W pliku `task.py` stwórz zmienne `a` i `b` przechowujące dowolne liczby. Sprawdź czy liczba `a` jest **większa** od `b` za pomocą odpowiedniego operatora. Zapisz wynik porównania w zmiennej `result`.

Wypisz tę zmienną w konsoli.

Przykładowy wynik (dla `a = 7` oraz `b = 13`):
```
False
```


## Zadanie 6 &ndash; Różnica wieku

W pliku `task.py` utwórz zmienną o nazwie `father` i nadaj jej wartość `1974`, oraz drugą zmienną o nazwie `child` i nadaj jej wartość `2007`.

Wypisz na konsolę komunikat (zamiast ###, wstaw różnicę wieku ojca i dziecka):
```
Ojciec jest starszy od dziecka o ### lat.
```

> ###### Podpowiedź: użyj konstrukcji `fstring` lub metody `format`.


## Zadanie 7 &ndash; Dzielenie

W pliku `task.py` utwórz zmienną `result` i nadaj jej wynik dzielenia 11 przez 7.

Wyświetl wynik w postaci:

```
11 : 7 = (tu wstaw wynik)
```

Zaokrąglij wynik do 2 miejsc po przecinku.

> ###### Podpowiedź: użyj funkcji `round`.


## Zadanie 8 &ndash; Wiek użytkownika

W pliku `task.py` napisz program, który:

* wyświetli na ekranie komunikat `Podaj swoje imię: `,
* pobierze z klawiatury imię użytkownika i zapisze go do zmiennej `name`,
* wyświetli na ekranie komunikat `Podaj rok swojego urodzenia: `,
* pobierze z klawiatury roku urodzenia użytkownika i zapisze go do zmiennej `year`,
* zamieni rok urodzenia użytkownika na liczbę,
* obliczy aktualny wiek użytkownika i zapisze go do zmiennej `age`,
* wyświetli na konsoli komunikat, w którym poda imię i aktualny wiek użytkownika:
```
Użytkownik: <name> jest w wieku <age> lat
```

**UWAGA:** zakładamy, że użytkownik jako rok swojego urodzenia poda poprawną liczbę!
