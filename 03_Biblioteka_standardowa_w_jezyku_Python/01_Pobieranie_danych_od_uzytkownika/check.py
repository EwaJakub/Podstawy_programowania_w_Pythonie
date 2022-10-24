import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Pobieranie danych od użytkownika")


@tc.test(
    "Skrypt pyta o imię i nazwisko oraz wyświetla tekst",
    params=(
        {"name": "Adam", "surname": "Mickiewicz"},
        {"name": "Juliusz", "surname": "Słowacki"},
    ),
)
def test_script(invoke, stdin, stdout, history, name, surname, **kwargs):
    stdin.append(name)
    stdin.append(surname)

    invoke()

    tc.assert_print_called(stdout)

    expected = "{} {} jest programistą Pythona".format(name, surname)

    if not any(expected.lower() in line.lower() for line in stdout):
        raise CodersLabException(
            dedent(
                """
                Oczekiwana fraza {} nie została znaleziona.
                Wypisany tekst:
                {}
                """
            ).format(p.b.get(expected), p.b.get("".join(h["text"] for h in history)))
        )


tc.run()
