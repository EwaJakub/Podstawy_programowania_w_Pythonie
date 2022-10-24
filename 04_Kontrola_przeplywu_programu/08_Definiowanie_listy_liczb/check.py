import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Definiowanie listy liczb")


@tc.test("Liczby są wypisywane na ekranie")
def test_print(invoke, stdout, **kwargs):
    invoke()

    for i in range(1, 9):
        try:
            next(l for l in stdout if "liczba: {}".format(i) in l.lower())
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Nie znaleziono frazy {} w tekście wypisywanym przez skrypt:
                    {}
                    """
                ).format(p.b.get("liczba: {}".format(i)), p.b.get("".join(stdout)))
            )

    try:
        next(l for l in stdout if "liczba: 0" in l.lower())
    except:
        pass
    else:
        raise CodersLabException(
            dedent(
                """
                Skrypt wypisał frazę {} która nie powinna się pojawić!
                """
            ).format(
                p.b.get("liczba: 0"),
            )
        )

    try:
        next(l for l in stdout if "liczba: 9" in l.lower())
    except:
        pass
    else:
        raise CodersLabException(
            dedent(
                """
                Skrypt wypisał frazę {} która nie powinna się pojawić!
                """
            ).format(
                p.b.get("liczba: 9"),
            )
        )


tc.run()
