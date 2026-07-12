# ThanviLang (TVL)
# AST
# Founder: Meeravali Velupuri

class ASTNode:
    pass


class Program(ASTNode):
    def __init__(self):
        self.statements = []


class StoreStatement(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class ShowStatement(ASTNode):
    def __init__(self, value):
        self.value = value


class Number(ASTNode):
    def __init__(self, value):
        self.value = value


class Identifier(ASTNode):
    def __init__(self, name):
        self.name = name
