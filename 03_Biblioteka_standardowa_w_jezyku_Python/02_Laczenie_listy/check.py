from ast import walk, Call, Attribute, Constant
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Łączenie listy")


@tc.test('Zmienna "letters" istnieje i ma oczekiwaną wartość', aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if "letters" not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get("letters")))

    if variables["letters"] != ["a", "b", "c", "d", "e"]:
        raise CodersLabException(
            dedent(
                """
                Oczekiwano, że zmienna {} będzie miała wartość {}.
                Jej obecna wartość to {}.
                """
            ).format(
                p.b.get("letters"),
                p.b.get(["a", "b", "c", "d", "e"]),
                p.b.get(variables["letters"]),
            )
        )


@tc.test('Metoda "join" została użyta')
def test_variable(ast, **kwargs):
    for node in walk(ast):
        if (
            isinstance(node, Call)
            and isinstance(node.func, Attribute)
            and node.func.attr == "join"
        ):
            return

    raise CodersLabException(
        dedent(
            """
            Nie znaleziono użycia metody {} które było wymagane w tym zadaniu.
            Przykład:
            {}
            {}
            """
        ).format(
            p.b.get("join"),
            p.b.get('>>> print(" && ".join(["A", "B", "CDE"]))'),
            p.b.get("A && B && CDE"),
        )
    )


@tc.test("Napis pojawia się na ekranie")
def test_print(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)

    if not any("a b c d e" in line for line in stdout):
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono oczekiwanej frazy {} w tekście wypisywanym na ekranie.
                Wypisany tekst:
                {}
                """
            ).format(
                p.b.get("a b c d e"),
                p.b.get("".join(stdout)),
            )
        )


tc.run()
