# ThanviLang (TVL)
# Parser Tests

from compiler.parser import Parser


def test_parser():
    source = """
@start

store x => 10

@stop
"""

    parser = Parser(source)
    parser.parse()

    print("Parser Test Passed")


if __name__ == "__main__":
    test_parser()
