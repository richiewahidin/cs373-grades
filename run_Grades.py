#!/usr/bin/env python3.11

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement

# -------------
# run_Grades.py
# -------------

# -------
# imports
# -------

import Grades

# -----------
# grades_read
# -----------

def grades_read () -> list[list[int]] :
    # read newline
    input()

    # read scores
    l_l_scores: list[list[int]] = [[int(s) for s in input().split()] for _ in range(5)]

    return l_l_scores

# ------------
# grades_print
# ------------

def grades_print (letter_grade: str) -> None :
    print(letter_grade)

# ----
# main
# ----

def main () -> None :
    # read number of test cases
    input()

    # read, eval, print (REPL)
    try :
        while True :
            l_l_scores: list[list[int]] = grades_read()
            letter:     str             = Grades.grades_eval(l_l_scores)
            grades_print(letter)
    except EOFError :
        pass

if __name__ == "__main__" : #pragma: no cover
    main()

"""
sample input

1

2 2 2 2 0
2 1 1 2 2 2 2 2 2 3 3 0
1 2 2 2 2 2 2 2 2 2 2 2 0 3
2 2 2 1 2 2 2 2 2 3 2 3 0 0
2 2 2 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 2 2 2 3 2 2 3 2 3 2 2 2 0 0 0 0 0 0 0 0
"""

"""
sample output

B-
"""
