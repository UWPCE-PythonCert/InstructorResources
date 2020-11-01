"""
tests for fizz buzz

NOTE: there is a lot of trickery in here to capture the print() output

Don't worry about understnding that at this point
"""


import contextlib
import io
import fizz_buzz

f = io.StringIO()
with contextlib.redirect_stdout(f):
    fizz_buzz.fizz_buzz(16)

output = f.getvalue()

expected_output = \
    """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
"""

assert output == expected_output, f"Expected output: {expected_output}"
