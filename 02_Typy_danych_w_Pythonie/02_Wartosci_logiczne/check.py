import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Wartości logiczne")


@tc.test(
    "Istnieje zmienna {name}",
    aborts=True,
    params=(
        {"name": "foo", "value": True},
        {"name": "bar", "value": False},
        {"name": "check", "value": False},
    ),
)
def test_variables(invoke, name, value, **kwargs):
    variables = invoke()

    if name not in variables:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono zmiennej o nazwie {}
                """
            ).format(p.b.get(name))
        )

    if variables[name] != value:
        raise CodersLabException(
            dedent(
                """
                Zmienna {} ma inną wartość niż przewiduje zadanie
                """
            ).format(p.b.get(name))
        )


@tc.test("Komunikat pojawia się na ekranie")
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

    if "Zmienna check ma wartość False\n" not in stdout:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie wypisał na ekranie komunikatu o odpowiedniej treści.
                Wypisane linie:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
