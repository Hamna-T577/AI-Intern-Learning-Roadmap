from typing import List
from decorators.logger_decorator import logger


@logger
def process_scores(scores: List[int]):

    double = lambda x: x * 2

    doubled_scores = list(map(double, scores))

    print("Doubled Scores:", doubled_scores)

    passed_scores = [
        score
        for score in doubled_scores
        if score >= 60
    ]

    print("Passed Scores:", passed_scores)

    score_dict = {
        index: value
        for index, value
        in enumerate(passed_scores)
    }

    print("Score Dictionary:", score_dict)

    sorted_scores = sorted(passed_scores)

    print("Sorted Scores:", sorted_scores)

    if 100 in sorted_scores:

        print("100 Found in List")

    else:

        print("100 Not Found")

    return sorted_scores