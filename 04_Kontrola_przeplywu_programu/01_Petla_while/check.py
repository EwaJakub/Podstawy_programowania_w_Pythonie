from ast import walk
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Pętla while")


@tc.test("Skrypt wypisuje tekst na ekranie")
def test_printing(invoke, stdout, **kwargs):
    invoke()

    if "Jestem programistą Pythona".lower() in "".join(stdout).lower():
        return

    if "Jestem programistką Pythona".lower() in "".join(stdout).lower():
        return

    tc.assert_print_called(stdout)

    raise CodersLabException(
        "Nie znaleziono oczekiwanej frazy w tekście, "
        "który skrypt wypisuje na ekranie"
    )


@tc.test("Skrypt wypisuje tekst na ekranie 10 razy")
def test_printing_10_times(invoke, stdout, **kwargs):
    invoke()

    string = "".join(stdout).lower()
    count = string.count("Jestem programistą Pythona".lower()) or string.count(
        "Jestem programistką Pythona".lower()
    )

    if count != 10:
        raise CodersLabException(
            "Tekst został wypisany {} razy, oczekiwano 10".format(count)
        )


tc.run()
