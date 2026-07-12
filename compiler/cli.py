# ThanviLang (TVL)
# Command Line Interface
# Founder: Meeravali Velupuri

import sys

VERSION = "0.1.0"


def main():
    if len(sys.argv) < 2:
        print("TVL Compiler")
        print("Usage:")
        print("  tvl version")
        print("  tvl run <file.tvl>")
        print("  tvl build <file.tvl>")
        return

    command = sys.argv[1]

    if command == "version":
        print(f"ThanviLang (TVL) {VERSION}")

    elif command == "run":
        if len(sys.argv) < 3:
            print("Error: Missing TVL file")
            return

        print(f"Running {sys.argv[2]}")

    elif command == "build":
        if len(sys.argv) < 3:
            print("Error: Missing TVL file")
            return

        print(f"Building {sys.argv[2]}")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
