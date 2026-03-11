import pytest
from testcases import parse_testcases
import os, subprocess, sys

SCRIPT = os.path.join(os.path.dirname(__file__), "oneliners.py")

TEST_CASES = parse_testcases("testcases.txt")

@pytest.mark.parametrize("name,input_lines,output_lines", TEST_CASES, ids=[c[0] for c in TEST_CASES])
def test_oneliners(name, input_lines, output_lines):
    stdin = "\n".join(input_lines) + "\n"
    result = subprocess.run(
        [sys.executable, SCRIPT],
        input=stdin,
        capture_output=True,
        text=True,
    )
    actual = result.stdout.splitlines()
    assert actual == output_lines, (
        f"\nTest case: {name}"
        f"\nExpected:\n" + "\n".join(output_lines) +
        f"\nActual:\n" + "\n".join(actual) +
        (f"\nStderr:\n{result.stderr}" if result.stderr else "")
    )
