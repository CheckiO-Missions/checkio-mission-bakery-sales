"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [100, 10, 4],
            "answer": "S",
        },
        {
            "input": [30, 45, 10],
            "answer": "C",
        },
        {
            "input": [3, 10, 5],
            "answer": "N",
        },
        {
            "input": [100, 0, 0],
            "answer": "B",
        },
    ],
    "Extra": [
        {
            "input": [10, 20, 30],
            "answer": "S",
        },
        {
            "input": [15, 82, 3],
            "answer": "C",
        },
        {
            "input": [96, 0, 1],
            "answer": "N",
        },
        {
            "input": [50, 10, 10],
            "answer": "B",
        },
    ]
}
