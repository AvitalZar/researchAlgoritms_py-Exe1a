"""
Functions for parsing and running testcases from the testcases.txt file.

Written by Claude Code.
"""

NUM_QUESTIONS = 8  # A through H


def parse_testcases(filename:str):
    """Parse testcases.txt into a list of (name, input_lines, output_lines)."""
    cases = []
    with open(filename) as f:
        lines = [line.rstrip("\n") for line in f]

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith("case="):
            i += 1
            continue

        name = line[len("case="):]
        i += 1

        # Skip optional metadata lines (e.g. "Fail message=...")
        while i < len(lines) and not lines[i].startswith("input="):
            i += 1

        if i >= len(lines):
            break

        # First input line has "input=" prefix
        input_lines = [lines[i][len("input="):]]
        i += 1
        # Remaining NUM_QUESTIONS-1 input lines
        for _ in range(NUM_QUESTIONS - 1):
            input_lines.append(lines[i])
            i += 1

        # First output line has "output=" prefix
        output_lines = [lines[i][len("output="):]]
        i += 1
        # Remaining NUM_QUESTIONS-1 output lines
        for _ in range(NUM_QUESTIONS - 1):
            output_lines.append(lines[i])
            i += 1

        cases.append((name, input_lines, output_lines))

    return cases


