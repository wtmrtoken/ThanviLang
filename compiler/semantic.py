def analyze(self, program):
    print("TVL Semantic Analyzer Started")

    statements = program.statements if hasattr(program, "statements") else program

    for statement in statements:
        if hasattr(statement, "name"):
            self.symbols[statement.name] = statement

    return True
