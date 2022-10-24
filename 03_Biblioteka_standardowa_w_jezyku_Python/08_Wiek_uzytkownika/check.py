import os
import sys
import datetime


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Wiek użytkownika")


@tc.test(
    "Skrypt pyta o imię i rok i zapisuje je w zmiennych",
    params=(
        {"name": "Kamila", "year": "1980"},
        {"name": "Marcin", "year": "1999"},
        {"name": "Jadwiga", "year": "1975"},
        {"name": "Ryszard", "year": "2002"},
    ),
    aborts=True,
)
def test_print(invoke, stdin, name, year, **kwargs):
    stdin.append(name)
    stdin.append(year)

    variables = invoke()

    for name, value in (("name", name), ("year", year)):
        if name not in variables:
            raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get(name)))
        if str(variables[name]) != value:
            raise CodersLabException(
                "Zmienna {} ma niepoprawną wartość".format(p.b.get(name))
            )


@tc.test(
    'Skrypt poprawnie oblicza wiek i zapisuje go w zmiennej "age"',
    params=(
        {"name": "Kamila", "year": "1980"},
        {"name": "Marcin", "year": "1999"},
        {"name": "Jadwiga", "year": "1975"},
        {"name": "Ryszard", "year": "2002"},
    ),
    aborts=True,
)
def test_print(invoke, stdin, name, year, **kwargs):
    stdin.append(name)
    stdin.append(year)

    variables = invoke()

    if "age" not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get("age")))
    if int(variables["age"]) != datetime.date.today().year - int(year):
        raise CodersLabException(
            "Zmienna {} ma niepoprawną wartość".format(p.b.get("age"))
        )


@tc.test(
    "Skrypt poprawnie wyświetla komunikat",
    params=(
        {"name": "Kamila", "year": "1980"},
        {"name": "Marcin", "year": "1999"},
        {"name": "Jadwiga", "year": "1975"},
        {"name": "Ryszard", "year": "2002"},
    ),
    aborts=True,
)
def test_print(invoke, stdin, stdout, history, name, year, **kwargs):
    stdin.append(name)
    stdin.append(year)

    variables = invoke()

    age = datetime.date.today().year - int(year)

    expected = "Użytkownik: {} jest w wieku {} lat".format(name, age)

    if expected not in "".join(stdout):
        raise CodersLabException(
            dedent(
                """
                Oczekiwana fraza {} nie została znaleziona.
                Wypisany tekst:
                {}
                """
            ).format(p.b.get(expected), p.b.get("".join(h["text"] for h in history)))
        )


tc.run()
