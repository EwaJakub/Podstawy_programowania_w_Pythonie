import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Różnica wieku")


@tc.test(
    'Zmienna "{name}" istnieje i ma wartość {value} typu int',
    params=(
        {"name": "father", "value": 1974},
        {"name": "child", "value": 2007},
    ),
    aborts=True,
)
def test_variables(invoke, name, value, **kwargs):
    variables = invoke()

    if name not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get(name)))

    if variables[name] != value:
        raise CodersLabException(
            "Zmienna {} ma niepoprawną wartość".format(p.b.get(name))
        )


@tc.test("Oczekiwany tekst wyświetla się na ekranie", aborts=True)
def test_print(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)

    if not any("Ojciec jest starszy od dziecka o 33 lat" in l for l in stdout):
        raise CodersLabException("Nie znaleziono oczekiwanego tekstu")


tc.run()
