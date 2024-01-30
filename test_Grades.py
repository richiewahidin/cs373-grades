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

import unittest  # main, TestCase

import Grades

# ----------------
# test_grades_eval
# ----------------


class test_grades_eval(unittest.TestCase):
    def test_0(self) -> None:
        l_l_scores: list[list[int]] = [[0, 0, 0, 0, 0]]
        letter: str = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "F")

    def test_1(self) -> None:
        l_l_scores: list[list[int]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        ]
        letter: str = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "F")

    def test_2(self) -> None:
        l_l_scores: list[list[int]] = [
            [1, 2, 3, 1, 2],
            [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
            [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],
            [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2],
            [
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
                1,
                2,
                3,
            ],
        ]
        letter: str = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "D+")

    def test_3(self) -> None:
        l_l_scores: list[list[int]] = [
            [0, 1, 2, 1, 1],
            [0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2],
            [0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1],
            [0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1],
            [
                0,
                1,
                2,
                1,
                1,
                2,
                0,
                1,
                2,
                1,
                1,
                2,
                0,
                1,
                2,
                1,
                1,
                2,
                0,
                1,
                2,
                1,
                1,
                2,
                0,
                1,
                2,
                1,
                1,
                2,
                0,
                1,
                2,
                1,
                1,
                2,
                0,
                1,
                2,
                1,
                1,
                2,
            ],
        ]
        letter: str = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "F")

    def test_4(self) -> None:
        l_l_scores: list[list[int]] = [
            [3, 2, 2, 2, 2],
            [3, 3, 2, 2, 2, 2, 3, 2, 2, 1, 3, 2],
            [3, 2, 2, 3, 2, 2, 3, 1, 2, 1, 3, 2, 3, 1],
            [3, 1, 2, 2, 2, 2, 3, 3, 2, 3, 2, 2, 3, 1],
            [
                3,
                2,
                2,
                3,
                1,
                2,
                3,
                3,
                2,
                3,
                3,
                2,
                3,
                1,
                2,
                3,
                3,
                2,
                3,
                1,
                2,
                1,
                3,
                2,
                3,
                1,
                2,
                2,
                1,
                2,
                3,
                3,
                2,
                1,
                1,
                2,
                3,
                1,
                2,
                1,
                1,
                2,
            ],
        ]
        letter: str = Grades.grades_eval(l_l_scores)
        self.assertEqual(letter, "A-")


class test_get_count(unittest.TestCase):
    def test_0(self) -> None:
        l_scores: list[int] = [3, 3, 3, 3, 0]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 4)

    def test_1(self) -> None:
        l_scores: list[int] = [2, 2, 2, 2, 2]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 5)

    def test_2(self) -> None:
        l_scores: list[int] = [3, 3, 1, 2, 2, 3, 2, 3, 1, 2, 2, 1]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 11)

    def test_3(self) -> None:
        l_scores: list[int] = [3, 1, 1, 2, 2, 3, 2, 1, 1, 2, 2, 1]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 8)

    def test_4(self) -> None:
        l_scores: list[int] = [2, 3, 2, 2, 1, 3, 1, 3, 2, 2, 3, 1, 3, 3]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 14)

    def test_5(self) -> None:
        l_scores: list[int] = [0, 3, 1, 1, 1, 3, 2, 0, 2, 2, 3, 1, 2, 2]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 9)

    def test_6(self) -> None:
        l_scores: list[int] = [2, 2, 3, 1, 2, 3, 2, 3, 3, 2, 1, 1, 2, 2]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 13)

    def test_7(self) -> None:
        l_scores: list[int] = [1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 3, 1]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 10)

    def test_8(self) -> None:
        l_scores: list[int] = [
            1,
            2,
            3,
            1,
            1,
            3,
            2,
            3,
            3,
            2,
            1,
            1,
            2,
            2,
            1,
            2,
            3,
            1,
            2,
            3,
            2,
            3,
            1,
            2,
            1,
            2,
            2,
            2,
            2,
            2,
            3,
            1,
            2,
            3,
            1,
            3,
            3,
            2,
            1,
            1,
            2,
            2,
        ]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 34)

    def test_9(self) -> None:
        l_scores: list[int] = [
            3,
            3,
            3,
            1,
            2,
            3,
            3,
            3,
            3,
            2,
            1,
            1,
            3,
            3,
            2,
            2,
            3,
            3,
            2,
            3,
            2,
            3,
            3,
            2,
            1,
            3,
            2,
            2,
            2,
            2,
            3,
            1,
            2,
            3,
            2,
            3,
            3,
            2,
            2,
            1,
            2,
            2,
        ]
        count: int = Grades.get_count(l_scores)
        self.assertEqual(count, 42)


class test_get_scores(unittest.TestCase):
    def test_0(self) -> None:
        grade: int = Grades.get_scores(4, Grades.THRESHOLDS[0])
        self.assertEqual(grade, 2)

    def test_1(self) -> None:
        grade: int = Grades.get_scores(5, Grades.THRESHOLDS[0])
        self.assertEqual(grade, 0)

    def test_2(self) -> None:
        grade: int = Grades.get_scores(11, Grades.THRESHOLDS[1])
        self.assertEqual(grade, 0)

    def test_3(self) -> None:
        grade: int = Grades.get_scores(8, Grades.THRESHOLDS[1])
        self.assertEqual(grade, 7)

    def test_4(self) -> None:
        grade: int = Grades.get_scores(14, Grades.THRESHOLDS[2])
        self.assertEqual(grade, 0)

    def test_5(self) -> None:
        grade: int = Grades.get_scores(9, Grades.THRESHOLDS[2])
        self.assertEqual(grade, 8)

    def test_6(self) -> None:
        grade: int = Grades.get_scores(13, Grades.THRESHOLDS[3])
        self.assertEqual(grade, 0)

    def test_7(self) -> None:
        grade: int = Grades.get_scores(10, Grades.THRESHOLDS[3])
        self.assertEqual(grade, 6)

    def test_8(self) -> None:
        grade: int = Grades.get_scores(34, Grades.THRESHOLDS[4])
        self.assertEqual(grade, 4)

    def test_9(self) -> None:
        grade: int = Grades.get_scores(42, Grades.THRESHOLDS[4])
        self.assertEqual(grade, 0)


# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
