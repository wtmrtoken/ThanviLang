# ThanviLang (TVL)
# Lexer Tests

from compiler.lexer import Lexer


def test_lexer():
    source = """
@start

store x => 10

show << x

@stop
"""

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    assert len(tokens) > 0

    print("Lexer Test Passed")


if __name__ == "__main__":
    test_lexer()
