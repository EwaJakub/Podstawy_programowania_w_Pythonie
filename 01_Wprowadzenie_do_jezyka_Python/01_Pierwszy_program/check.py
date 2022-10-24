import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Pierwszy program")


@tc.test("Funkcja print została użyta", aborts=True)
def test_print(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)


@tc.test("Wypisany tekst zaczyna się od frazy podanej w poleceniu", aborts=True)
def test_print_value(invoke, stdout, **kwargs):
    invoke()

    if not any("Mam na imię" in line for line in stdout):
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono oczekiwanej frazy {} w tekście wypisywanym na ekranie.
                Wypisany tekst:
                {}
                """
            ).format(
                p.b.get("Mam na imię"),
                p.b.get("".join(stdout)),
            )
        )


tc.run()
