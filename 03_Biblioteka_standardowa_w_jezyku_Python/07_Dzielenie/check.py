import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Dzielenie")


@tc.test('Zmienna "result" istnieje i ma wartość 1.5714...', aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if "result" not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get("result")))

    if variables["result"] != 11 / 7 and variables["result"] != round(11 / 7, 2):
        raise CodersLabException(
            "Zmienna {} ma niepoprawną wartość".format(p.b.get("result"))
        )


@tc.test("Działanie pojawia się na ekranie")
def test_print(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)

    if not any("11 : 7 = 1.57" in line for line in stdout):
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono oczekiwanej frazy {} w tekście wypisywanym na ekranie.
                Wypisany tekst:
                {}
                """
            ).format(
                p.b.get("11 : 7 = 1.57"),
                p.b.get("".join(stdout)),
            )
        )


tc.run()
