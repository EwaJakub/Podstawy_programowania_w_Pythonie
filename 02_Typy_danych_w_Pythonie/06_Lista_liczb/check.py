import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Lista liczb")


@tc.test('Zmienna "numbers" istnieje', aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if "numbers" not in variables:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono zmiennej {}
                """
            ).format(p.b.get("numbers"))
        )


@tc.test('Zmienna "numbers" zawiera liczby od 1 do 8', aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if variables["numbers"] != [1, 2, 3, 4, 5, 6, 7, 8]:
        raise CodersLabException(
            dedent(
                """
                Zmienna {} zawiera inne dane niż podane w poleceniu zadania.
                """
            ).format(p.b.get("numbers"))
        )


@tc.test("Przedostatnia liczba jest wypisana na ekranie", aborts=True)
def test_variable(invoke, stdout, **kwargs):
    invoke()

    if not stdout:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie wypisał żadnego tekstu na ekranie.
                Czy funkcja {} została użyta?
                """
            ).format(p.b.get("print"))
        )

    if stdout != ["7\n"]:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie wypisał oczekiwanej liczby (7) na ekranie. Wypisano linie:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
