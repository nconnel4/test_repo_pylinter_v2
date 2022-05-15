import math
import os


def sub(a, b) -> int:
    return math.floor(a - b)


def word_count(sentence, w) -> int:
    sentence = sentence.lower().split()
    if w in sentence:
        return sum([1 for x in sentence if x == w])
    else:
        return 0
