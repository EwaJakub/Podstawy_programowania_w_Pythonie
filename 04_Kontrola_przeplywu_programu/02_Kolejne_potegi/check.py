from ast import walk, For
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Kolejne potęgi")


@tc.test("Skrypt wypisuje zdania na ekranie", aborts=True)
def test_printing(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)

    for num in range(11):
        phrase = "2 do potęgi {} to {}".format(num, 2 ** num)
        if phrase not in "".join(stdout).lower():
            raise CodersLabException("Nie znaleziono frazy {}".format(p.b.get(phrase)))


@tc.test("Pętla for była użyta do wykonania zadania", aborts=True)
def test_for_used(ast, **kwargs):
    for node in walk(ast):
        if isinstance(node, For):
            break

    else:
        raise CodersLabException(
            "W zadaniu nie znaleziono pętli {}".format(p.b.get("for"))
        )


tc.run()
