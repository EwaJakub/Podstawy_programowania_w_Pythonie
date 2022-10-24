import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Porównywanie liczb")


@tc.test("Liczby są zapamiętywane w zmiennych a i b", aborts=True)
def test_a_b(invoke, stdin, **kwargs):
    stdin.append("123456")
    stdin.append("345678")

    variables = invoke()

    if "a" not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get("a")))

    if "b" not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get("b")))

    if str(variables["a"]).split('.')[0] != "123456":
        raise CodersLabException(
            "Liczba wprowadzona z klawiatury nie została zapamiętana "
            "w zmiennej {}".format(p.b.get("a"))
        )

    if str(variables["b"]).split('.')[0] != "345678":
        raise CodersLabException(
            "Liczba wprowadzona z klawiatury nie została zapamiętana "
            "w zmiennej {}".format(p.b.get("b"))
        )


@tc.test(
    "Liczby {a} i {b} są poprawnie porównane",
    params=[
        {"a": "123", "b": "456", "greater": "b"},
        {"a": "456", "b": "123", "greater": "a"},
    ],
    aborts=True,
)
def test_comparison_lex(invoke, stdin, stdout, a, b, greater, history, **kwargs):
    stdin.append(a)
    stdin.append(b)

    invoke()

    tc.assert_print_called(stdout)

    if "{} jest większe!".format(greater) not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                W wypisanym tekście nie znaleziono frazy {}

                Wypisane linie:
                {}
                """
            ).format(
                p.b.get("{} jest większe!".format(greater)),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


@tc.test(
    "Liczby {a} i {b} są poprawnie porównane",
    params=[
        {"a": "123", "b": "56", "greater": "a", "smaller": "b"},
        {"a": "99", "b": "789", "greater": "b", "smaller": "a"},
    ],
    aborts=True,
)
def test_comparison_as_number(
    invoke, stdin, stdout, a, b, greater, smaller, history, **kwargs
):
    stdin.append(a)
    stdin.append(b)

    invoke()

    wrong = "{} jest większe!".format(smaller)

    if wrong in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                W wypisanym tekście znaleziono (niepoprawny) wynik: {}
                Prawdopodobnie dlatego, że porównano wprowadzone dane jako stringi
                a nie jako liczby.
                "{}" wygląda na większe od "{}" bo "{}" jest dalej niż "{}"
                w "komputerowym alfabecie".

                Aby porównać je jako liczby, użyj funkcji {}.

                Przykład:
                >>> a = "12"
                >>> b = "34"
                >>> a + b
                "1234"
                >>> float(a) + float(b)
                46

                """
            ).format(
                p.b.get(wrong),
                p.b.get(min(a, b)),
                p.b.get(max(a, b)),
                p.b.get(str(max(a, b))[0]),
                p.b.get(str(min(a, b))[0]),
                p.b.get("float"),
            )
        )

    correct = "{} jest większe!".format(greater)


tc.run()
