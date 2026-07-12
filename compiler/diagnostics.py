# ThanviLang (TVL)
# Diagnostics System
# Founder: Meeravali Velupuri

from enum import Enum


class Severity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Diagnostic:

    def __init__(self, code, severity, message, line=0, column=0):
        self.code = code
        self.severity = severity
        self.message = message
        self.line = line
        self.column = column

    def __str__(self):
        return (
            f"[{self.severity.value}] "
            f"{self.code}: {self.message} "
            f"(Line {self.line}, Column {self.column})"
        )


class DiagnosticCollector:

    def __init__(self):
        self.diagnostics = []

    def report(self, code, severity, message, line=0, column=0):
        self.diagnostics.append(
            Diagnostic(code, severity, message, line, column)
        )

    def has_errors(self):
        return any(
            d.severity == Severity.ERROR
            for d in self.diagnostics
        )

    def print_all(self):
        for diagnostic in self.diagnostics:
            print(diagnostic)
