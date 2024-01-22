#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = missing-docstring

# --------------
# test_Grades.py
# --------------

# -------
# imports
# -------

import unittest # main, TestCase

import Grades

# ----------------
# test_grades_eval
# ----------------

class test_grades_eval (unittest.TestCase) :
    def test_0 (self) -> None :
        l_l_scores: list[list[int]] = [[0, 0, 0, 0, 0]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "B-")

# ----
# main
# ----

if __name__ == "__main__" : #pragma: no cover
    unittest.main()
