# ThanviLang (TVL) Compiler
# TVL Virtual Machine (TVM)
# Founder: Meeravali Velupuri

class TVM:
    def __init__(self):
        self.variables = {}

    def execute(self, bytecode):
        print("TVL Virtual Machine Started")

        for instruction in bytecode:
            opcode, operand = instruction

            if opcode == "STORE":
                self.variables[operand] = None
                print(f"[STORE] {operand}")

            elif opcode == "PRINT":
                print(f"[OUTPUT] {operand}")

        print("TVM Execution Completed")
