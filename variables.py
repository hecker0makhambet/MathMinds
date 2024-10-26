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

# tasks = [[[f"Concept {i}", f"Task {i}"], f"A{i}", f"B{i}", f"C{i}", f"D{i}", random.choice(range(1, 5))] for i in range(100)]

tasks = [
    [
        [f"Formulas", f"(cos^2(a)) / (cos^2(a) - 1)"],
        "-tg^2(a)",
        "-ctg^2(a)",
        "ctg(a)",
        "1 - tg^2(a)",
        2
    ],
    [
        [f"Trigonometry", f"(1 - sin^2(a)) / (1 - cos^2(a))"],
        "-ctg^2(a)",
        "tg^2(a)",
        "tg^2(a)",
        "ctg^2(a)",
        4
    ],
    [
        [f"Concept {0}", f"sin(a) / tg(a)"],
        "-cos(a)",
        "sin(a)",
        "sin^2(a) * cos(a)",
        "cos(a)",
        4
    ],
    [
        [f"Concept {0}", f"1 / (1 + cos(a))) + 1 / (1 - cos^2(a))"],
        "tg^2(a)",
        "1",
        "2/sin^2(a)",
        "2/cos^2(a)",
        3
    ],
    [
        [f"Concept {0}", f"(1 - tg(-a)) / (sin(a) + cos(a))"],
        "1 / cos(a)",
        "-1 / sin(a)",
        "1 / sin(a)",
        "1 + tg(a)",
        1
    ],
    [
        [f"Concept {0}", f"1 - ctg^2(П/6)"],
        "1",
        "4",
        "2",
        "0",
        2
    ],
    [
        [f"Concept {0}", f"tg(a) * cos(a) + sin(a)"],
        "2*sin(a)",
        "2*cos(a)",
        "-3*cos(a)",
        "0",
        1
    ],
    [
        [f"Formulas", "tg(a) + ctg(a)"],
        "A",
        "B",
        "C",
        "D",
        2
    ]
]


concepts = [
    [
        "Formulas",
        "Basic Formulas",
        [
            "sin (-a) = -sin a",
            "cos (-a) = cos a",
            "tg (-a) = -tg a",
            "ctg (-a) = -ctg a",
            "sin^2(a) + cos^2(a) = 1"
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
    [
        "Solid geometry",
        "Trigonometriesesbabe",
        [
            "list of cdasasdasdasards",
            "formula1",
            "formula2"
        ]
    ],
    [
        "Planimetry",
        "Trigonometriesesbabe",
        [
            "list of cdasasdasdasards",
            "formula1",
            "formula2"
        ]
    ],
    [
        "Algebra",
        "Algebra",
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