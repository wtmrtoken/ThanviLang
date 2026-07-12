# ThanviLang (TVL) Compiler
# Main Entry
# Founder: Meeravali Velupuri

from parser import Parser
from semantic import SemanticAnalyzer
from type_checker import TypeChecker
from bytecode import BytecodeGenerator
from tvm import TVM


def main():
    source = """
@start

show << "Welcome to ThanviLang"

@stop
"""

    parser = Parser(source)
    ast = parser.parse()

    semantic = SemanticAnalyzer()
    semantic.analyze(ast)

    checker = TypeChecker()
    checker.check(ast)

    generator = BytecodeGenerator()
    bytecode = generator.generate(ast)

    vm = TVM()
    vm.execute(bytecode)


if __name__ == "__main__":
    main()
