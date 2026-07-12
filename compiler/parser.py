# ThanviLang (TVL)
# Parser
# Founder: Meeravali Velupuri

from lexer import Lexer


class Parser:

    def __init__(self, source):
        self.tokens = Lexer(source).tokenize()
        self.position = 0

    def current(self):
        return self.tokens[self.position]

    def advance(self):
        self.position += 1

    def parse(self):
        print("TVL Parser Started")
        return self.tokens
