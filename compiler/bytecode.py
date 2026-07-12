# ThanviLang (TVL)
# Bytecode Generator
# Founder: Meeravali Velupuri

class BytecodeGenerator:

    def __init__(self):
        self.instructions = []

    def emit(self, opcode, operand=None):
        self.instructions.append((opcode, operand))

    def generate(self, ast):
        print("TVL Bytecode Generator Started")

        # TODO: Walk the AST and generate bytecode

        return self.instructions
