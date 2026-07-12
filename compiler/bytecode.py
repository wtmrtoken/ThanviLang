# ThanviLang (TVL) Compiler
# Bytecode Generator
# Founder: Meeravali Velupuri

class BytecodeGenerator:
    def __init__(self):
        self.bytecode = []

    def emit(self, opcode, operand=None):
        self.bytecode.append((opcode, operand))

    def generate(self, ast):
        print("TVL Bytecode Generator Started")

        for node in ast.body:
            self.visit(node)

        print("Bytecode generation completed.")
        return self.bytecode

    def visit(self, node):
        node_type = type(node).__name__

        if node_type == "Variable":
            self.emit("STORE", node.name)

        elif node_type == "Print":
            self.emit("PRINT", node.value)
