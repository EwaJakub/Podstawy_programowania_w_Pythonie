import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Dodawanie")


@tc.test("Istnieje zmienna add1 typu int")
def test_add1(invoke, **kwargs):
    variables = invoke()

    if "add1" not in variables:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono zmiennej {}
                """
            ).format(p.b.get("add1"))
        )

    if type(variables["add1"]) != int:
        raise CodersLabException(
            dedent(
                """
                Zmienna {} nie ma wartości typu {}.
                """
            ).format(p.b.get("add1"), p.b.get("int"))
        )


@tc.test("Istnieje zmienna add2 typu float")
def test_add1(invoke, **kwargs):
    variables = invoke()

    if "add2" not in variables:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono zmiennej {}
                """
            ).format(p.b.get("add2"))
        )

    if type(variables["add2"]) != float:
        raise CodersLabException(
            dedent(
                """
                Zmienna {} nie ma wartości typu {}.
                """
            ).format(p.b.get("add2"), p.b.get("float"))
        )


@tc.test("Istnieje zmienna result z wynikiem dodawania")
def test_result(invoke, **kwargs):
    variables = invoke()

    if "result" not in variables:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono zmiennej {}
                """
            ).format(p.b.get("result"))
        )

    if variables["result"] != variables["add1"] + variables["add2"]:
        raise CodersLabException(
            dedent(
                """
                Zmienna {} ma inny wynik niż oczekiwano - jej wartość to {}
                """
            ).format(p.b.get("result"), p.b.get(variables["result"]))
        )


@tc.test("Wynik jest wypisywany na ekranie")
def test_print(invoke, stdout, **kwargs):
    variables = invoke()

    if not stdout:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie wypisał żadnego tekstu na ekranie.
                Czy funkcja {} została użyta?
                """
            ).format(p.b.get("print"))
        )

    if str(variables["result"]) + "\n" not in stdout:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie wypisał na ekranie komunikatu o odpowiedniej treści.
                Oczekiwano tylko wyniku dodawania.

                Wypisane linie:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
