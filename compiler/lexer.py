# ThanviLang (TVL)
# Lexer
# Founder: Meeravali Velupuri

from tokens import Token, TokenType


class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0

    def tokenize(self):
        tokens = []

        words = self.source.split()

        for word in words:
            if word == "store":
                tokens.append(Token(TokenType.STORE, word, 1))
            elif word == "show":
                tokens.append(Token(TokenType.SHOW, word, 1))
            elif word.isdigit():
                tokens.append(Token(TokenType.NUMBER, int(word), 1))
            else:
                tokens.append(Token(TokenType.IDENTIFIER, word, 1))

        tokens.append(Token(TokenType.EOF, "", 1))
        return tokens
