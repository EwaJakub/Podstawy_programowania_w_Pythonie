import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Operacje matematyczne")


@tc.test(
    "Istnieje zmienna {name} o odpowiedniej wartości",
    params=(
        {"name": "a1", "value": 25},
        {"name": "a2", "value": 10},
        {"name": "sum_value", "value": 35},
        {"name": "quotus", "value": 2.5},
        {"name": "int_part", "value": 2},
    ),
    aborts=False,
)
def test_variables(invoke, name, value, **kwargs):
    variables = invoke()
    if name not in variables:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono zmiennej {}
                """
            ).format(p.b.get(name))
        )

    if variables[name] != value:
        raise CodersLabException(
            dedent(
                """
                Zmienna {} ma inną wartość niż oczekiwano
                """
            ).format(p.b.get(name))
        )


@tc.test("Wypisywanie wartości na ekranie")
def test_print(invoke, stdout, **kwargs):
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

    if stdout != ["25\n", "10\n", "35\n", "2.5\n", "2\n"]:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie wypisał oczekiwanej treści na ekranie. Wypisano linie:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
