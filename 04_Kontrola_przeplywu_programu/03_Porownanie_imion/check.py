import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Porównywanie imion")


@tc.test(
    "Zapisywanie imienia do zmiennej {name}",
    params=[
        {"name": "first_name", "value": "PierwszeImieTestowe"},
        {"name": "second_name", "value": "DrugieImieTestowe"},
    ],
    aborts=True,
)
def test_variables(invoke, stdin, name, value, **kwargs):
    stdin.append("PierwszeImieTestowe")
    stdin.append("DrugieImieTestowe")

    variables = invoke()

    if name not in variables:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie stworzył zmiennej {}
                """
            ).format(p.b.get(name))
        )

    if variables[name] != value:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie zapamiętał imienia wprowadzonego z klawiatury do zmiennej {}
                """
            ).format(p.b.get(name))
        )


@tc.test(
    "Imiona {name1} oraz {name2}",
    params=[
        {"name1": "Atos", "name2": "Atos", "same": True},
        {"name1": "Portos", "name2": "Portos", "same": True},
        {"name1": "Aramis", "name2": "Aramis", "same": True},
        {"name1": "Zbyszko", "name2": "Maćko", "same": False},
        {"name1": "Zbyszko", "name2": "Jurand", "same": False},
        {"name1": "Jurand", "name2": "Maćko", "same": False},
    ],
    aborts=True,
)
def test_same_names(invoke, stdin, stdout, history, name1, name2, same, **kwargs):
    stdin.append(name1)
    stdin.append(name2)

    invoke()

    tc.assert_print_called(stdout)

    if "Podaj pierwsze imię".lower() not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Wygląda na to że skrypt nie zapytał o pierwsze imię.
                Oczekiwano, że na ekranie pojawi się napis {}

                Skrypt wypisuje tekst:
                {}
                """
            ).format(
                p.b.get("Podaj pierwsze imię"),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )

    if "Podaj drugie imię".lower() not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Wygląda na to że skrypt nie zapytał o drugie imię.
                Oczekiwano, że na ekranie pojawi się napis {}

                Skrypt wypisuje tekst:
                {}
                """
            ).format(
                p.b.get("Podaj drugie imię"),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )

    expected = "Takie same" if same else "Różne"

    if expected.lower() not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Wygląda na to że skrypt nie wyświetlił wyniku porównania.
                Oczekiwano, że na ekranie pojawi się napis {}

                Skrypt wypisuje tekst:
                {}
                """
            ).format(
                p.b.get(expected),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


tc.run()
