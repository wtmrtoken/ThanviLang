# ThanviLang (TVL) Compiler
# AST (Abstract Syntax Tree)
# Founder: Meeravali Velupuri

class ASTNode:
    def __init__(self, node_type):
        self.node_type = node_type

class Program(ASTNode):
    def __init__(self):
        super().__init__("Program")
        self.body = []

class Variable(ASTNode):
    def __init__(self, name, value):
        super().__init__("Variable")
        self.name = name
        self.value = value

class Print(ASTNode):
    def __init__(self, value):
        super().__init__("Print")
        self.value = value
