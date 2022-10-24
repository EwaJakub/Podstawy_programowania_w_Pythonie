from ast import walk, Call, Attribute, Constant
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Dzielenie modulo")


@tc.test('Zmienne "a", "b" oraz "result" istnieją', aborts=True)
def test_variables(invoke, **kwargs):
    variables = invoke()

    for name in ("a", "b", "result"):
        if name not in variables:
            raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get(name)))

        if not isinstance(variables[name], (int, float)):
            raise CodersLabException(
                dedent(
                    """
                    Oczekiwano, że zmienna {} będzie miała wartość typu {} lub {}.
                    Jej obecna typ to {}.
                    """
                ).format(
                    p.b.get(name),
                    p.b.get("int"),
                    p.b.get("float"),
                    p.b.get(type(variables[name]).__name__),
                )
            )


@tc.test('Zmienna "result" ma odpowiednią wartość')
def test_variables(invoke, **kwargs):
    variables = invoke()

    if variables["a"] % variables["b"] != variables["result"]:
        raise CodersLabException(
            dedent(
                """
                Dla a={} oraz b={} oczekiwano że wartością zmiennej {} będzie {}.
                Jej obecna wartość to {}.
                """
            ).format(
                p.b.get(variables["a"]),
                p.b.get(variables["b"]),
                p.b.get("result"),
                p.b.get(variables["a"] % variables["b"]),
                p.b.get(variables["result"]),
            )
        )


tc.run()
