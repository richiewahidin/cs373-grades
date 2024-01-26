#!/usr/bin/env python2

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
        self.assertEqual(letter, "F")
    def test_1 (self) -> None :
        l_l_scores: list[list[int]] = [[0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "F")
    def test_2 (self) -> None :
        l_l_scores: list[list[int]] = [[1, 3, 1, 3, 1],
                                       [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
                                       [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
                                       [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3],
                                       [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "D+")
    def test_3 (self) -> None :
        l_l_scores: list[list[int]] = [[1, 2, 3, 1, 2],
                                       [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
                                       [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],
                                       [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],
                                       [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "D+")
    def test_4 (self) -> None :
        l_l_scores: list[list[int]] = [[1, 2, 3, 2, 2],
                                       [1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3],
                                       [1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 2],
                                       [1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 2],
                                       [1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 2, 3, 2, 2, 3]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "B+")
    def test_5 (self) -> None :
        l_l_scores: list[list[int]] = [[0, 1, 2, 1, 1],
                                       [0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2],
                                       [0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1],
                                       [0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1],
                                       [0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "F")
    def test_6 (self) -> None :
        l_l_scores: list[list[int]] = [[3, 1, 2, 2, 2],
                                       [3, 3, 2, 2, 1, 2, 3, 2, 2, 1, 3, 2],
                                       [3, 1, 2, 3, 2, 2, 3, 1, 2, 1, 1, 2, 3, 1],
                                       [3, 1, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 3, 1],
                                       [3, 2, 2, 1, 1, 2, 3, 3, 2, 1, 3, 2, 3, 1, 2, 3, 3, 2, 3, 1, 2, 1, 1, 2, 3, 1, 2, 2, 1, 2, 3, 3, 2, 1, 1, 2, 3, 1, 2, 1, 1, 2]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "B-")
    def test_7 (self) -> None :
        l_l_scores: list[list[int]] = [[3, 2, 2, 2, 2],
                                       [3, 3, 2, 2, 2, 2, 3, 2, 2, 1, 3, 2],
                                       [3, 2, 2, 3, 2, 2, 3, 1, 2, 1, 3, 2, 3, 1],
                                       [3, 1, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 3, 1],
                                       [3, 2, 2, 3, 1, 2, 3, 3, 2, 3, 3, 2, 3, 1, 2, 3, 3, 2, 3, 1, 2, 1, 3, 2, 3, 1, 2, 2, 1, 2, 3, 3, 2, 1, 1, 2, 3, 1, 2, 1, 1, 2]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "A-")
    def test_8 (self) -> None :
        l_l_scores: list[list[int]] = [[3, 2, 2, 2, 2],
                                       [3, 3, 2, 2, 2, 2, 3, 2, 2, 3, 3, 2],
                                       [3, 2, 2, 3, 2, 2, 3, 2, 2, 1, 3, 2, 3, 1],
                                       [3, 1, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 3, 3],
                                       [3, 2, 2, 3, 1, 2, 3, 3, 2, 3, 3, 2, 3, 1, 2, 3, 3, 2, 3, 1, 2, 1, 3, 2, 3, 3, 2, 2, 0, 2, 3, 3, 2, 1, 1, 2, 3, 1, 2, 1, 1, 2]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "A")
    def test_9 (self) -> None :
        l_l_scores: list[list[int]] = [[2, 2, 2, 2, 2],
                                       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                                       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                                       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                                       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0]]
        letter:     str             = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "A")

class test_get_scores (unittest.TestCase) :
    def test_0 (self) -> None :
        l_scores: list[int] = [3, 3, 3, 3, 0]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[0])
        self.assertEqual(grade, 2)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "B+")
    def test_1 (self) -> None :
        l_scores: list[int] = [2, 2, 2, 2, 2]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[0])
        self.assertEqual(grade, 0)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "A")
    def test_2 (self) -> None :
        l_scores: list[int] = [3, 3, 1, 2, 2]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[0])
        self.assertEqual(grade, 0)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "A")
    def test_3 (self) -> None :
        l_scores: list[int] = [3, 3, 1, 2, 2, 3, 2, 3, 1, 2, 2, 1]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[1])
        self.assertEqual(grade, 0)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "A")
    def test_4 (self) -> None :
        l_scores: list[int] = [3, 1, 1, 2, 2, 3, 2, 1, 1, 2, 2, 1]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[1])
        self.assertEqual(grade, 7)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "C-")
    def test_5 (self) -> None :
        l_scores: list[int] = [3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 2, 1]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[1])
        self.assertEqual(grade, 11)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "F")
    def test_6 (self) -> None :
        l_scores: list[int] = [2, 3, 2, 2, 1, 3, 1, 3, 2, 2, 3, 1, 3, 3]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[2])
        self.assertEqual(grade, 0)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "A")
    def test_7 (self) -> None :
        l_scores: list[int] = [0, 3, 1, 1, 1, 3, 2, 0, 2, 2, 3, 1, 2, 2]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[2])
        self.assertEqual(grade, 8)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "D+")
    def test_8 (self) -> None :
        l_scores: list[int] = [1, 2, 2, 1, 1, 3, 2, 0, 2, 2, 1, 1, 2, 2]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[2])
        self.assertEqual(grade, 10)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "D-")
    def test_9 (self) -> None :
        l_scores: list[int] = [2, 2, 3, 1, 2, 3, 2, 3, 3, 2, 1, 1, 2, 2]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[3])
        self.assertEqual(grade, 0)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "A")
    def test_10 (self) -> None :
        l_scores: list[int] = [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 1]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[3])
        self.assertEqual(grade, 6)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "C")
    def test_11 (self) -> None :
        l_scores: list[int] = [3, 0, 0, 1, 0, 1, 0, 3, 3, 3, 1, 1, 2, 1]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[3])
        self.assertEqual(grade, 11)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "F")
    def test_12 (self) -> None :
        l_scores: list[int] = [1, 2, 3, 1, 1, 3, 2, 3, 3, 2, 1, 1, 2, 2, 1, 2, 3, 1, 2, 3, 2, 3, 1, 2, 1, 2, 2, 2, 2, 2, 3, 1, 2, 3, 1, 3, 3, 2, 1, 1, 2, 2]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[4])
        self.assertEqual(grade, 4)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "B-")
    def test_13 (self) -> None :
        l_scores: list[int] = [3, 3, 3, 1, 2, 3, 3, 3, 3, 2, 1, 1, 3, 3, 2, 2, 3, 3, 2, 3, 2, 3, 3, 2, 1, 3, 2, 2,2, 2, 3, 1, 2, 3, 2, 3, 3, 2, 2, 1, 2, 2]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[4])
        self.assertEqual(grade, 0)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "A")
    def test_14 (self) -> None :
        l_scores: list[int] = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
        grade: int          = Grades.get_scores(l_scores, Grades.THRESHOLDS[4])
        self.assertEqual(grade, 10)
        letter: str         = Grades.GRADES[grade]
        self.assertEqual(letter, "D-")
# ----
# main
# ----

if __name__ == "__main__" : #pragma: no cover
    unittest.main()
