import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Typy danych")


@tc.test(
    "Istnieje zmienna z danymi typu {name}",
    params=(
        {"name": "int", "type_": int},
        {"name": "float", "type_": float},
        {"name": "bool", "type_": bool},
        {"name": "str", "type_": str},
    ),
)
def test_variables(invoke, name, type_, **kwargs):
    variables = invoke()

    types = {type(value) for value in variables.values()}

    if type_ not in types:
        raise CodersLabException(
            """
            Nie znaleziono żadnej zmiennej typu {}
            """.format(
                p.b.get(name)
            )
        )


@tc.test("Wypisywanie nazw i wartości zmiennych na ekranie", points=5)
def test_printing(invoke, stdout, **kwargs):
    variables = invoke()

    tc.assert_print_called(stdout)

    relevant_lines = [line for line in stdout if line.startswith("Zmienna")]
    if not relevant_lines:
        raise CodersLabException(
            """
            Nie znaleziono żadnej linii, która zaczynałaby się od słowa "Zmienna"
            wśród linii:
            {}
            """.format(
                p.b.get("".join(stdout))
            )
        )

    mentioned_variables = []
    for line in relevant_lines:
        try:
            mentioned_variables.append(line.split()[1])
        except IndexError:
            raise CodersLabException(
                dedent(
                    """
                    Z wypisanej na ekranie linii:
                    {}
                    nie udało się odczytać, której zmiennej dotyczy
                    """
                ).format(p.b.get(line))
            )

    for name in mentioned_variables:
        if not any(
            line.split()[:4] == ["Zmienna", name, "ma", "wartość"]
            for line in relevant_lines
        ):
            raise CodersLabException(
                dedent(
                    """
                    Wśród wypisanych linii:
                    {}
                    nie znaleziono takiej, która zaczynałaby się od:
                    {}
                    """
                ).format(
                    p.b.get("".join(stdout)),
                    p.b.get("Zmienna {} ma wartość".format(name)),
                )
            )
    if len(mentioned_variables) != 4:
        raise CodersLabException(
            """
            Oczekiwano wypisania czterech zmiennych, znaleziono {}: {}
            """.format(
                len(mentioned_variables), ", ".join(mentioned_variables)
            )
        )

    for name in mentioned_variables:
        if name not in variables:
            raise CodersLabException(
                dedent(
                    """
                    Na ekranie wypisano wartość zmiennej {} której nie udało się
                    znaleźć w kodzie... literówka?
                    """
                ).format(p.b.get(name))
            )

        real_value = variables[name]
        relevant_line = next(
            line
            for line in relevant_lines
            if line.split()[:4] == ["Zmienna", name, "ma", "wartość"]
        )

        if not relevant_line.strip().endswith(str(real_value).strip()):
            raise CodersLabException(
                dedent(
                    """
                    Zmienna {} ma wartość:
                    {}
                    ale na ekranie wypisano że jej wartość to:
                    {}
                    """
                ).format(
                    p.b.get(name),
                    p.b.yellow.get(real_value),
                    p.b.yellow.get("".join(relevant_line.split(maxsplit=4)[4:])),
                )
            )


tc.run()
