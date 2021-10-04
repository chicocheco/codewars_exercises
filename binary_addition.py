"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

best voted solution:
def add_binary(a,b):
    return bin(a+b)[2:]
"""


def add_binary(a, b):
    return bin(a + b).replace("0b", "")
