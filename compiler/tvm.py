# ThanviLang (TVL)
# TVL Virtual Machine (TVM)
# Founder: Meeravali Velupuri

class TVM:

    def __init__(self):
        self.stack = []
        self.variables = {}

    def execute(self, instructions):
        print("TVL Virtual Machine Started")

        for opcode, operand in instructions:

            if opcode == "PUSH":
                self.stack.append(operand)

            elif opcode == "STORE":
                self.variables[operand] = self.stack.pop()

            elif opcode == "LOAD":
                self.stack.append(self.variables.get(operand))

            elif opcode == "PRINT":
                print(self.stack.pop())

        print("Execution Finished")
