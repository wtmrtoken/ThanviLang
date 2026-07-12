# ThanviLang (TVL) Compiler
# Type Checker
# Founder: Meeravali Velupuri

from ast import Variable, Print

class TypeChecker:
    def __init__(self):
        self.types = {}

    def check(self, ast):
        print("TVL Type Checker Started")

        for node in ast.body:
            self.visit(node)

        print("Type checking completed.")
        return True

    def visit(self, node):
        if isinstance(node, Variable):
            value = node.value

            if isinstance(value, int):
                self.types[node.name] = "int"
            elif isinstance(value, float):
                self.types[node.name] = "float"
            elif isinstance(value, str):
                self.types[node.name] = "string"
            elif isinstance(value, bool):
                self.types[node.name] = "bool"
            else:
                self.types[node.name] = "unknown"

        elif isinstance(node, Print):
            pass
