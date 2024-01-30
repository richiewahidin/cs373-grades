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

# Constant tuple that stores the final grades to be returned per set of scores
GRADES = ("A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F")

# Each list of tuple(int, int) represents the first occurrence of a score and
# the grade index associated with it. There is a different list associated with
# each kind of assignment, i.e. projects, quizzes, etc. Thresholds is therefore
# a list of list of tuples
THRESHOLDS = [
    [(5, 0), (4, 2), (3, 8), (0, 11)],
    [(11, 0), (10, 2), (9, 5), (8, 7), (7, 10), (0, 11)],
    [(13, 0), (12, 2), (11, 4), (10, 6), (9, 8), (8, 10), (0, 11)],
    [(13, 0), (12, 2), (11, 4), (10, 6), (9, 8), (8, 10), (0, 11)],
    [
        (39, 0),
        (38, 1),
        (37, 2),
        (35, 3),
        (34, 4),
        (32, 5),
        (31, 6),
        (29, 7),
        (28, 8),
        (27, 9),
        (25, 10),
        (0, 11),
    ],
]

# Constants for each individual score (except 0 since it's unnecessary)
EXCELLENT = 3
MEETS_EXPECTATIONS = 2
REVISION_NEEDED = 1


# helper method that gets the count of passing scores from a list of scores
def get_count(scores: list[int]) -> int:
    # counters for the number of ones, threes, and total passing scores
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
    add_to_pass = min(
        one_counter, three_counter // 2
    )  # adds to the passing score the min of number of ones and the number of threes divided by two
    pass_counter += add_to_pass
    return pass_counter


# helper method that returns the score related to a certain count based on a
# particular list of thresholds for a category
def get_scores(count: int, thresholds: list[tuple[int, int]]) -> int:
    index = 0

    # goes through the thresholds to find the highest grade index for that score
    while index < len(thresholds) - 1 and thresholds[index][0] > count:
        index += 1
    return thresholds[index][1]


def grades_eval(l_l_scores: list[list[int]]) -> str:
    assert l_l_scores
    final_score = 0
    for index, l_scores in enumerate(l_l_scores):
        # get_scores gets the score for each category, and the final score is
        # the min of all the scores for each category
        count = get_count(l_scores)
        score = get_scores(count, THRESHOLDS[index])
        final_score = max(score, final_score)
    return GRADES[final_score]
