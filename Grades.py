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
grades = ("A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-")


def get_scores(scores: list[int], thresholds: tuple[int, int, int, int, int, int, int, int, int, int, int]) -> int :
    pass_counter = 0
    for curr_score in scores:
        if curr_score >= 2:
            pass_counter += 1

    index = 0
    while index < len(thresholds) - 1 and thresholds[index] > pass_counter:
        index += 1
    return index

def get_scores_with_redemption(scores: list[int], thresholds: tuple[int, int, int, int, int, int, int, int, int, int, int]) -> int :
    pass_counter = 0
    one_counter = 0
    three_counter = 0
    for curr_score in scores:
        if curr_score >= 2:
            pass_counter += 1
            if curr_score == 3:
                three_counter += 1
        elif curr_score == 1:
            one_counter += 1
    index = 0
    add_to_pass = max(one_counter, three_counter // 2)
    pass_counter += add_to_pass
    while index < len(thresholds) - 1 and thresholds[index] > pass_counter:
        index += 1
    return index

def grades_eval (l_l_scores: list[list[int]]) -> str :
    assert l_l_scores
    thresholds = ((5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3),
                  (11, 11, 10, 10, 10, 9, 9, 8, 8, 8, 7),
                  (13, 13, 12, 12, 11, 11, 10, 10, 9, 9, 8),
                  (13, 13, 12, 12, 11, 11, 10, 10, 9, 9, 8),
                  (39, 38, 37, 35, 34, 32, 21, 29, 28, 27, 25))
    final_score = 0
    for index, l_scores in enumerate(l_l_scores):
        if index in (1, 3, 4):
            score = get_scores_with_redemption(l_scores, thresholds[index])
        else:
            score = get_scores(l_scores, thresholds[index])
        final_score = max(score, final_score)
    return grades[final_score]
