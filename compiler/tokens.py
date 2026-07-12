# ThanviLang (TVL)
# Token Definitions
# Founder: Meeravali Velupuri

from enum import Enum, auto


class TokenType(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()

    STORE = auto()
    SHOW = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FUNCTION = auto()
    RETURN = auto()

    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    ASSIGN = auto()

    LPAREN = auto()
    RPAREN = auto()

    EOF = auto()


class Token:
    def __init__(self, token_type, value, line):
        self.type = token_type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"{self.type.name}({self.value})"
