import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Tabliczka mnożenia")


@tc.test(
    "Tabliczka jest wypisywana na ekranie",
    params=(
        {"n": 1},
        {"n": 2},
        {"n": 3},
        {"n": 4},
        {"n": 5},
    ),
)
def test_print(invoke, stdin, stdout, history, n, **kwargs):
    stdin.append(str(n))

    invoke()

    for i in range(1, 11):
        expected = "{} * {} = {}".format(i, n, i * n)
        try:
            next(filter(lambda l: expected in l, stdout))
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Nie znaleziono frazy {} w wypisywanym przez skrypt tekście:
                    {}
                    """
                ).format(
                    p.b.get(expected), p.b.get("".join(h["text"] for h in history))
                )
            )


tc.run()
