#!/usr/bin/env python3

# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long

# ---------
# Grades.py
# ---------

# https://docs.python.org/3.6/library/functools.html
# https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html

# -----------
# grades_eval
# -----------

GRADES = ("A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")
WORST_GRADE = 11
THRESHOLDS = [[(5, 0), (4, 2), (3,8), (0, 11)],
              [(11, 0), (10, 2), (9, 5), (8, 7), (7, 10), (0, 11)],
              [(13, 0), (12, 2), (11, 4), (10, 6), (9, 8), (8, 10), (0, 11)],
              [(13, 0), (12, 2), (11, 4), (10, 6), (9, 8), (8, 10), (0, 11)],
              [(39, 0), (38, 1), (37, 2), (35, 3), (34, 4), (32, 5), (31, 6), (29, 7), (28, 8), (27, 9), (25, 10), (0, 11)]]
EXCELLENT = 3
MEETS_EXPECTATIONS = 2
REVISION_NEEDED = 1


def get_scores(scores: list[int], thresholds: list[tuple[int, int]]) -> int :
    pass_counter = 0
    one_counter = 0
    three_counter = 0
    for curr_score in scores:
        if curr_score >= MEETS_EXPECTATIONS:
            pass_counter += 1
            if curr_score == EXCELLENT:
                three_counter += 1
        elif curr_score == REVISION_NEEDED:
            one_counter += 1
    index = 0
    add_to_pass = min(one_counter, three_counter // 2)
    pass_counter += add_to_pass
    index = 0
    while index < len(thresholds) - 1 and thresholds[index][0] > pass_counter:
        index += 1
    return thresholds[index][1]

def grades_eval (l_l_scores: list[list[int]]) -> str :
    assert l_l_scores
    final_score = 0
    for index, l_scores in enumerate(l_l_scores):
        score = get_scores(l_scores, THRESHOLDS[index])
        final_score = max(score, final_score)
    return GRADES[final_score]
