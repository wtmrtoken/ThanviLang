# ThanviLang (TVL)
# Semantic Analyzer
# Founder: Meeravali Velupuri

class SemanticAnalyzer:

    def __init__(self):
        self.symbols = {}

    def analyze(self, program):
        print("TVL Semantic Analyzer Started")

        for statement in program.statements:
            if hasattr(statement, "name"):
                self.symbols[statement.name] = statement

        return True
