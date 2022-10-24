import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Równanie kwadratowe")


@tc.test(
    "Liczby {a}, {b}, {c} są zapamiętywane w zmiennych a, b i c",
    params=[
        {"a": "12345", "b": "23456", "c": "34567"},
        {"a": "33443", "b": "44554", "c": "55665"},
        {"a": "-5", "b": "-10", "c": "-15"},
    ],
    aborts=True,
)
def test_a_b_c(invoke, stdin, a, b, c, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    for name, value in [("a", a), ("b", b), ("c", c)]:
        if name not in variables:
            raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get(name)))

        if str(variables[name]) not in (value, value + ".0"):
            raise CodersLabException(
                ("Zmienna {} ma inną wartość niż wprowadzona z klawiatury").format(
                    p.b.get(name)
                )
            )

        if type(variables[name]) == int:
            raise CodersLabException(
                dedent(
                    """
                    Zmienna {} ma wartość typu {}. To lepiej niż {}, ale co jeśli
                    ktoś zechce wprowadzić wartość x = 5.25?
                    """
                ).format(
                    p.b.get(name),
                    p.b.get("int"),
                    p.b.get("str"),
                )
            )

        if type(variables[name]) == str:
            raise CodersLabException(
                dedent(
                    """
                    Zmienna {} ma wartość typu {}.
                    Polecenie zadania wymaga, aby w zmiennej {} pojawiła się
                    wartość rzutowana na odpowiedni typ, aby dało się na niej
                    wykonywać operacje matematyczne.
                    """
                ).format(
                    p.b.get(name),
                    p.b.get("str"),
                    p.b.get(name),
                )
            )

        if type(variables[name]) != float:
            raise CodersLabException(
                dedent(
                    """
                    Zmienna {} ma wartość typu {}.
                    Polecenie zadania wymaga, aby w zmiennej {} pojawiła się
                    wartość rzutowana na odpowiedni typ, aby dało się na niej
                    wykonywać operacje matematyczne.
                    """
                ).format(
                    p.b.get(name),
                    p.b.get(type(variables[name]).__name__),
                    p.b.get(name),
                )
            )


@tc.test(
    "Obliczanie delty dla parametrów {a}, {b} i {c}",
    params=[
        {"a": "2", "b": "6", "c": "3", "delta": 12.0},
        {"a": "2", "b": "5", "c": "3", "delta": 1.0},
        {"a": "1", "b": "8", "c": "16", "delta": 0.0},
        {"a": "2", "b": "4", "c": "3", "delta": -8.0},
    ],
    aborts=True,
)
def test_delta(invoke, stdin, a, b, c, delta, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    if "delta" not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get("delta")))

    if variables["delta"] != delta:
        raise CodersLabException(
            dedent(
                """
                Niepoprawna wartość zmiennnej {}.
                Skrypt obliczył wartość: {}
                a oczekiwano: {}
                """
            ).format(
                p.b.get("delta"),
                p.b.get(variables["delta"]),
                p.b.get(delta),
            )
        )


@tc.test(
    "Obliczanie wartości zmiennych x_1 i x_2 dla parametrów {a}, {b} i {c}",
    params=[
        {"a": "5", "b": "9", "c": "4", "delta": 1, "x1": -1.0, "x2": -0.8},
        {"a": "2", "b": "-7", "c": "6", "delta": 1, "x1": 1.5, "x2": 2},
        {"a": "9", "b": "6", "c": "1", "delta": 0, "x1": -1/3, "x2": -1/3},
    ],
    aborts=True,
)
def test_x1_x2(invoke, stdin, stdout, a, b, c, delta, x1, x2, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    for name, value in (("x_1", x1), ("x_2", x2)):
        if name not in variables:
            raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get(name)))

        if variables[name] != value:
            raise CodersLabException(
                dedent(
                    """
                    Niepoprawna wartość zmiennnej {}.
                    Skrypt obliczył wartość: {}
                    a oczekiwano: {}
                    """
                ).format(
                    p.b.get(name),
                    p.b.get(variables[name]),
                    p.b.get(value),
                )
            )


@tc.test(
    "Wyświetlanie wyniku dla parametrów {a}, {b} i {c} (delta dodatnia)",
    params=[
        {"a": "5", "b": "9", "c": "4", "delta": 1, "x1": -1.0, "x2": -0.8},
        {"a": "2", "b": "-7", "c": "6", "delta": 1, "x1": 1.5, "x2": 2},
    ],
    aborts=True,
)
def test_print_x1_x2(invoke, stdin, stdout, history, a, b, c, delta, x1, x2, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    tc.assert_print_called(stdout)

    for name, value in (("x_1", x1), ("x_2", x2)):
        if "{} = {}".format(name, value) not in "".join(stdout).lower():
            raise CodersLabException(
                dedent(
                    """
                    Nie znaleziono wyniku w tekście. Oczekiwano linii: {}
                    Wypisane linie:
                    {}
                    """
                ).format(
                    p.b.get("{} = {}".format(name, value)),
                    p.b.get("".join(h.get("text", "") for h in history)),
                )
            )


@tc.test(
    "Wyświetlanie wyniku dla parametrów {a}, {b} i {c} (delta zerowa)",
    params=[
        {"a": "9", "b": "6", "c": "1", "x": -1/3},
        {"a": "4", "b": "-4", "c": "1", "x": 0.5},
    ],
    aborts=True,
)
def test_print_x12(invoke, stdin, stdout, history, a, b, c, x, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    tc.assert_print_called(stdout)

    if "x_1 = x_2 = {}".format(x) not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono wyniku w tekście. Oczekiwano linii: {}
                Wypisane linie:
                {}
                """
            ).format(
                p.b.get("x_1 = x_2 = {}".format(x)),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


@tc.test(
    "Wyświetlanie wyniku dla parametrów {a}, {b} i {c} (delta ujemna)",
    params=[
        {"a": "9", "b": "6", "c": "2"},
        {"a": "4", "b": "-4", "c": "2"},
    ],
    aborts=True,
)
def test_no_solution(invoke, stdin, stdout, history, a, b, c, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    tc.assert_print_called(stdout)

    if "brak rozwiązań" not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono wyniku w tekście. Oczekiwano linii: {}
                Wypisane linie:
                {}
                """
            ).format(
                p.b.get("brak rozwiązań"),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


tc.run()
