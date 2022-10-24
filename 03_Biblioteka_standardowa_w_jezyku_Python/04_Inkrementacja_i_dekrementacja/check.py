from ast import walk, AugAssign, Add, Sub
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Inkrementacja i dekrementacja")


@tc.test("Tekst jest wypisywany na ekranie", aborts=True)
def test_variables(invoke, stdout, **kwargs):
    variables = invoke()

    tc.assert_print_called(stdout)

    for expected in ("145", "146"):
        if not any(expected in line for line in stdout):
            raise CodersLabException(
                "Nie znaleziono liczby {} w wypisywanym tekście".format(
                    p.b.get(expected)
                )
            )

    if "counter" not in variables:
        raise CodersLabException(
            "Nie znaleziono zmiennej {}".format(p.b.get("counter"))
        )

    if variables["counter"] != 145:
        raise CodersLabException(
            dedent(
                """
                Po zakończeniu skryptu zmienna {} powinna mieć wartość {}.
                Jej obecna wartość to {}.
                """
            ).format(
                p.b.get("counter"),
                p.b.get("145"),
                p.b.get(variables["counter"]),
            )
        )


@tc.test(
    "Użyto operatora {op}",
    params=(
        {"op": "+=", "cls": Add},
        {"op": "-=", "cls": Sub},
    ),
)
def test_variables(ast, op, cls, **kwargs):
    for node in walk(ast):
        if isinstance(node, AugAssign) and isinstance(node.op, cls):
            return

    raise CodersLabException(
        dedent(
            """
            Operator {} nie został znaleziony w kodzie.
            """
        ).format(
            p.b.get(op),
        )
    )


tc.run()
