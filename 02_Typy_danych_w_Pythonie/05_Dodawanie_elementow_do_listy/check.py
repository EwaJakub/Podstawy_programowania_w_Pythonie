import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Dodawanie elementów do listy")


@tc.test("Lista ma 3 elementy")
def test_length(invoke, **kwargs):
    variables = invoke()

    if "animals" not in variables:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono zmiennej {}
                """
            ).format(p.b.get("animals"))
        )

    if type(variables["animals"]) != list:
        raise CodersLabException(
            dedent(
                """
                Zmienna {} nie jest listą
                """
            ).format(p.b.get("animals"))
        )

    if len(variables["animals"]) != 3:
        raise CodersLabException(
            dedent(
                """
                Zmienna {} nie ma 3 elementów. Ma {}!
                """
            ).format(p.b.get("animals"), p.b.get(len(variables["animals"])))
        )


tc.run()
