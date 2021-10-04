"""
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""


def high_and_low(numbers):
    ints = [int(i) for i in numbers.split(' ')]
    return f'{str(max(ints))} {str(min(ints))}'


print(high_and_low('325 379 -873 -129 902 214 106 -685 -498 299 793 339 736 126 -553'))
