"""
TESTS is a dict with all your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['What is >apple<', '>', '<'],
            "answer": 'apple'
        },
        {
            "input": ['What is [apple]', '[', ']'],
            "answer": 'apple'
        },
        {
            "input": ['What is ><', '>', '<'],
            "answer": ''
        },
        {
            "input": ['[an apple]', '[', ']'],
            "answer": 'an apple'
        }
    ],
    "Extra": [
        {
            "input": ['>Apple< is simple', '>', '<'],
            "answer": 'apple'
        }
    ]
}
