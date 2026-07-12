# ThanviLang (TVL)
# Code Formatter
# Founder: Meeravali Velupuri

class Formatter:

    def format(self, source):

        lines = source.splitlines()
        output = []

        for line in lines:
            output.append(line.strip())

        return "\n".join(output)
