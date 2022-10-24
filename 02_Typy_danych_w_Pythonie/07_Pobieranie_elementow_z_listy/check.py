import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Lista liczb")


@tc.test('Zmienna "characters" wciąż istnieje', aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if "characters" not in variables:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono zmiennej {}
                """
            ).format(p.b.get("characters"))
        )


@tc.test(
    "{which} postać jest wypisana na ekranie",
    params=(
        {"which": "Pierwsza", "character": "Harry"},
        {"which": "Ostatnia", "character": "Hermione"},
    ),
    aborts=False,
)
def test_variable(invoke, stdout, character, **kwargs):
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

    if character + "\n" not in stdout:
        raise CodersLabException(
            dedent(
                """
                Wskazana osoba nie została wypisana na ekranie. Wypisano linie:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
