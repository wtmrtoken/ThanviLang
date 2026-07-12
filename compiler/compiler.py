# ThanviLang (TVL)
# Compiler Pipeline
# Founder: Meeravali Velupuri

from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from type_checker import TypeChecker
from bytecode import BytecodeGenerator


class Compiler:

    def __init__(self):
        pass

    def compile(self, source):

        print("TVL Compiler Started")

        lexer = Lexer(source)
        tokens = lexer.tokenize()

        parser = Parser(source)
        ast = parser.parse()

        semantic = SemanticAnalyzer()
        semantic.analyze(ast)

        checker = TypeChecker()
        checker.check(ast)

        generator = BytecodeGenerator()
        bytecode = generator.generate(ast)

        print("Compilation Successful")

        return bytecode
