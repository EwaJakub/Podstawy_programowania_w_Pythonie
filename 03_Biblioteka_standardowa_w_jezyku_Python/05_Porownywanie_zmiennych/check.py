import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Porównywanie zmiennych")


@tc.test(
    'Zmienna "{name}" istnieje',
    params=(
        {"name": "a"},
        {"name": "b"},
        {"name": "result"},
    ),
    aborts=True,
)
def test_variables(invoke, name, **kwargs):
    variables = invoke()

    if name not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get(name)))


@tc.test('Zmienna "result" zawiera wynik porównania za pomocą operatora >', aborts=True)
def test_result(invoke, **kwargs):
    variables = invoke()

    if variables["result"] != (variables["a"] > variables["b"]):
        raise CodersLabException(
            "Niepoprawna wartość zmiennej {}".format(p.b.get("result"))
        )


tc.run()
