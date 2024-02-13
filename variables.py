# tasks = {
#     0: [
#         ["Concept1", "Task1"],
#         "A",
#         "B",
#         "C",
#         "D",
#         1  # Correct answer
#     ],
#     1: [
#         ["Concept2", "Task2"],
#         "A",
#         "B",
#         "C",
#         "D",
#         4
#     ]
# }

import random

tasks = [[[f"Concept {i}", f"Task {i}"], f"A{i}", f"B{i}", f"C{i}", f"D{i}", random.choice(range(1, 5))] for i in range(100)]

concepts = [
    [
        "Formulas",
        "Basice Formulas",
        [
            "list of cards"
        ]
    ],
    [
        "Trigonometry",
        "Trigonometriesesbabe",
        [
            "list of cdasasdasdasards",
            "formula1",
            "formula2"
        ]
    ],
]

# concepts = {
#     "Formulas": [
#         "Formula",
#         "BASICUS FORMULASE",
#         [
#             "list of cards"
#         ]
#     ],
#     "Trigonometry": [
#         "Trigonometriese",
#         "BASICUS TRIGONOMETRIUS",
#         "CONTENTUSE TRIGONOMETRIUSE"
#     ]
# }