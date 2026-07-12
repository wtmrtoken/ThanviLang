# ThanviLang (TVL)
# Error Definitions
# Founder: Meeravali Velupuri

class TVLError(Exception):

    def __init__(self, code, message, line=0, column=0):
        self.code = code
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.__str__())

    def __str__(self):
        return (
            f"{self.code}: {self.message} "
            f"(Line {self.line}, Column {self.column})"
        )


class LexerError(TVLError):
    pass


class ParserError(TVLError):
    pass


class SemanticError(TVLError):
    pass


class TypeError(TVLError):
    pass


class RuntimeError(TVLError):
    pass
