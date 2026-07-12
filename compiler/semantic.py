# ThanviLang (TVL) Compiler
# Semantic Analyzer
# Founder: Meeravali Velupuri

from ast import Program, Variable, Print

class SemanticAnalyzer:
    def __init__(self):
        self.symbols = {}

    def analyze(self, ast):
        print("TVL Semantic Analyzer Started")

        if isinstance(ast, Program):
            for node in ast.body:
                self.visit(node)

        print("Semantic analysis completed.")
        return True

    def visit(self, node):
        if isinstance(node, Variable):
            if node.name in self.symbols:
                raise Exception(f"Duplicate variable: {node.name}")
            self.symbols[node.name] = node.value

        elif isinstance(node, Print):
            pass
