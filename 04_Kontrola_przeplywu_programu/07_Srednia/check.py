import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Średnia liczb")


@tc.test(
    'Podana z klawiatury ilość liczb: {n}, jest zapamiętana w zmiennej "n"',
    params=[
        {"n": "4"},
        {"n": "12"},
        {"n": "60"},
    ],
    aborts=True,
)
def test_n(stdin, stdout, invoke, n, **kwargs):
    stdin.append(n)
    stdin.extend(["123"] * int(n))

    variables = invoke()

    if "n" not in variables:
        raise CodersLabException("Nie znaleziono zmiennej {}".format(p.b.get("n")))

    if str(variables["n"]) != n:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie zapamiętał liczby wprowadzonej z klawiatury do zmiennej {}
                Zmienna {} ma wartość {} zamiast oczekiwanej {}
                """
            ).format(
                p.b.get("n"),
                p.b.get("n"),
                p.b.get(variables["n"]),
                p.b.get(n),
            )
        )


@tc.test(
    'Skrypt czyta z klawiatury {n} liczb i zapisuje do listy "numbers"',
    params=[
        {"n": "6", "numbers": ["1", "3", "9", "35", "11", "2"]},
        {"n": "7", "numbers": ["5", "15", "6", "4", "6", "7", "0"]},
        {"n": "8", "numbers": ["3", "6", "4", "6", "7", "8", "-20", "-10"]},
    ],
    aborts=True,
)
def test_n(stdin, stdout, invoke, n, numbers, **kwargs):
    stdin.append(n)
    stdin.extend(numbers)

    variables = invoke()

    if len(stdin) == int(n):
        raise CodersLabException("Skrypt nie wczytał liczb z klawiatury")

    if stdin:
        raise CodersLabException(
            dedent(
                """
                Skrypt nie wczytał wszystkich liczb z klawiatury.
                Oczekiwano że skrypt zapyta o {} liczb, a zapytał tylko o {}.
                """
            ).format(p.b.get(int(n)), p.b.get(int(n) - len(stdin)))
        )

    if "numbers" not in variables:
        raise CodersLabException(
            "Nie znaleziono zmiennej {}".format(p.b.get("numbers"))
        )

    if type(variables["numbers"]) != list:
        raise CodersLabException(
            dedent(
                """
                Oczekiwano że wartość zmiennej {} będzie typu {} - jej typ to {}
                """
            ).format(
                p.b.get("numbers"),
                p.b.get("list"),
                p.b.get(type(variables["numbers"]).__name__),
            )
        )


@tc.test(
    "Skrypt czyta z klawiatury {n} liczb i wyświetla sumę oraz średnią",
    params=[
        {"n": "6", "numbers": ["1", "3", "9", "35", "11", "2"]},
        {"n": "7", "numbers": ["5", "15", "6", "4", "6", "7", "0"]},
        {"n": "8", "numbers": ["3", "6", "4", "6", "7", "8", "-20", "-50"]},
    ],
    aborts=True,
)
def test_n(stdin, stdout, invoke, n, numbers, history, **kwargs):
    stdin.append(n)
    stdin.extend(numbers)

    variables = invoke()

    try:
        line = next(line for line in stdout if "suma" in line.lower())
    except StopIteration:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono słowa {} w wypisywanym na ekranie tekście:
                {}
                """
            ).format(p.b.get("Suma"), p.b.get("".join(h["text"] for h in history)))
        )

    try:
        sum_value = float("".join(c for c in line if c in "0123456789.-"))
    except:
        raise CodersLabException(
            dedent(
                """
            Nie udało się odczytać sumy w linii: {}
        """
            ).format(p.b.get(line))
        )

    try:
        line = next(line for line in stdout if "średnia" in line.lower())
    except StopIteration:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono słowa {} w wypisywanym na ekranie tekście:
                {}
                """
            ).format(p.b.get("Średnia"), p.b.get("".join(h["text"] for h in history)))
        )

    try:
        avg_value = float("".join(c for c in line if c in "0123456789.-"))
    except:
        raise CodersLabException(
            dedent(
                """
                Nie udało się odczytać średniej w linii: {}
                """
            ).format(p.b.get(line))
        )

    expected_sum = sum(map(int, numbers))
    expected_avg = expected_sum / int(n)

    if sum_value != expected_sum:
        raise CodersLabException(
            dedent(
                """
                Skrypt twierdzi że suma liczb {} to {}.
                Oczekiwano odpowiedzi {}
                """
            ).format(
                p.b.get(", ".join(numbers)),
                p.b.get(sum_value),
                p.b.get(expected_sum),
            )
        )

    if avg_value != expected_avg:
        raise CodersLabException(
            dedent(
                """
                Skrypt twierdzi że średnia liczb {} to {}.
                Oczekiwano odpowiedzi {}
                """
            ).format(
                p.b.get(", ".join(numbers)),
                p.b.get(avg_value),
                p.b.get(expected_avg),
            )
        )

    if expected_avg > expected_sum:
        expected = "średnia jest większa"
    else:
        expected = "suma jest większa"

    try:
        next(line for line in stdout if expected in line.lower())
    except:
        raise CodersLabException(
            dedent(
                """
                Nie znaleziono linii {} w wypisywanym przez skrypt tekście:
                {}
                """
            ).format(
                p.b.get(expected),
                p.b.get("".join(h["text"] for h in history)),
            )
        )


tc.run()
