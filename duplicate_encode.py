"""The goal of this exercise is to convert a string to a new string where each character in the new string is
"(" if that character appears only once in the original string, or ")" if that character appears more than once
in the original string. Ignore capitalization when determining if a character is a duplicate.


NOTES:
don't forget lowercase it.
"""


def duplicate_encode(word: str):
    # your code here
    ret = ''
    low_word = word.lower()
    for i in low_word:
        if low_word.count(i) == 1:
            ret += '('
        else:
            ret += ')'
    return ret


