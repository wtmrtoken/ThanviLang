# ThanviLang (TVL) Compiler
# Parser
# Founder: Meeravali Velupuri

from lexer import Lexer

class Parser:
    def __init__(self, source):
        self.lexer = Lexer(source)
        self.tokens = self.lexer.tokenize()

    def parse(self):
        print("TVL Parser Started")
        return {
            "type": "Program",
            "body": []
        }
