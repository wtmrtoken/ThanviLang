# ThanviLang (TVL)
# Interpreter
# Founder: Meeravali Velupuri

from ast import Program, StoreStatement, ShowStatement


class Interpreter:

    def __init__(self):
        self.variables = {}

    def execute(self, program):

        print("TVL Interpreter Started")

        if not isinstance(program, Program):
            return

        for statement in program.statements:
            self.visit(statement)

        print("Program Finished")

    def visit(self, node):

        if isinstance(node, StoreStatement):
            self.variables[node.name] = node.value

        elif isinstance(node, ShowStatement):

            value = node.value

            if hasattr(value, "name"):
                print(self.variables.get(value.name))

            elif hasattr(value, "value"):
                print(value.value)

            else:
                print(value)
