import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("FizzBuzz")


@tc.test("Oczekiwane liczby są wypisywane na ekranie")
def test_numbers(invoke, stdout, **kwargs):
    invoke()

    expected = [str(n) for n in range(1, 101) if n % 3 and n % 5]

    it = iter(stdout)

    for e in expected:
        try:
            while e not in next(it):
                pass
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Nie znaleziono oczekiwanej linii: {}
                    Wypisane linie:
                    {}
                    """
                ).format(
                    p.b.get(e),
                    p.b.get("".join(stdout)),
                )
            )


@tc.test('Fraza "Fizz" jest wypisywana w odpowiednich miejscach na ekranie')
def test_numbers(invoke, stdout, **kwargs):
    invoke()

    expected = ["Fizz" if n % 3 == 0 else str(n) for n in range(1, 101) if n % 5]

    it = iter(stdout)

    for e in expected:
        try:
            while e not in next(it):
                pass
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Nie znaleziono oczekiwanej linii: {}
                    Wypisane linie:
                    {}
                    """
                ).format(
                    p.b.get(e),
                    p.b.get("".join(stdout)),
                )
            )


@tc.test('Fraza "Buzz" jest wypisywana w odpowiednich miejscach na ekranie')
def test_numbers(invoke, stdout, **kwargs):
    invoke()

    expected = ["Buzz" if n % 5 == 0 else str(n) for n in range(1, 101) if n % 3]

    it = iter(stdout)

    for e in expected:
        try:
            while e not in next(it):
                pass
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Nie znaleziono oczekiwanej linii: {}
                    Wypisane linie:
                    {}
                    """
                ).format(
                    p.b.get(e),
                    p.b.get("".join(stdout)),
                )
            )


@tc.test('Fraza "FizzBuzz" jest wypisywana w odpowiednich miejscach na ekranie')
def test_numbers(invoke, stdout, **kwargs):
    invoke()

    expected = [
        "FizzBuzz" if n % 5 == n % 3 == 0 else str(n)
        for n in range(1, 101)
        if n % 5 == n % 3 == 0 or n % 5 and n % 3
    ]

    it = iter(stdout)

    for e in expected:
        try:
            while e not in next(it):
                pass
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Nie znaleziono oczekiwanej linii: {}
                    Wypisane linie:
                    {}
                    """
                ).format(
                    p.b.get(e),
                    p.b.get("".join(stdout)),
                )
            )


tc.run()
