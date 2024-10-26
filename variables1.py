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
        "Basic formulas",
        [
            [
                'text',
                [f'Basic formulas A level', f'(cos(a) / tg(a)'],
                'ctg(a)'
            ],
            [
                'test',
                [f"Basic Formulas  A level", f"(cos^2(a)) / (cos^2(a) - 1)"],
                "-tg^2(a)",
                "-ctg^2(a)",
                "ctg(a)",
                "1 - tg^2(a)",
                2,
            ],
            [
                'test',
                [f"Basic Formulas  A level", f"sin(a) / tg(a)"],
                "-cos(a)",
                "sin(a)",
                "sin^2(a) * cos(a)",
                "cos(a)",
                4
            ],
            [
                'test',
                [f"Basic Formulas  B level", f"tg(a) * cos(a) + sin(a)"],
                "2*sin(a)",
                "2*cos(a)",
                "-3*cos(a)",
                "0",
                1
            ],
            [
                'test',
                [f"Basic Formulas B level", "sin^2(25) + cos^2(25) + 5"],
                "6",
                "5,5",
                "4",
                "7",
                1
            ],
            [
                'test',
                [f"Basic Formulas  B level", f"(1 - sin^2(a)) / (1 - cos^2(a))"],
                "-ctg^2(a)",
                "tg^2(a)",
                "tg^2(a)",
                "ctg^2(a)",
                4
            ],
            [
                'test',
                [f"Basic Formulas  C level", f"tg^2(a) - sin^2(a) - tg^2(a)sin^2(a)"],
                "-1",
                "1",
                "0",
                "-2",
                3
            ],
            [
                'test',
                [f"Basic Formulas  C level", f"2sin^2(a) - 1 + cos^2(a)"],
                "sin^2(a)",
                "3sin^2(a)",
                "cos^2(a)",
                "-2cos^2(a)",
                1
            ],
            [
                'test',
                [f"Basic Formulas  C level", f"1 / (1 + cos(a))) + 1 / (1 - cos^2(a))"],
                "tg^2(a)",
                "1",
                "2/sin^2(a)",
                "2/cos^2(a)",
                3
            ],
        ]
    ],
    [
        'Cofunction Identities',
        [
            [
                'test',
                [f"Cofunction Identities A level", f"tg(27) * tg(63)"],
                "tg^2(27)",
                "1",
                "ctg^2(27)",
                "-1",
                2
            ],
        ]
    ],
    [
        'Concept {0}',
        [
            [
                'test',
                [f"Concept {0}", f"(1 - tg(-a)) / (sin(a) + cos(a))"],
                "1 / cos(a)",
                "-1 / sin(a)",
                "1 / sin(a)",
                "1 + tg(a)",
                1
            ],
            [
                'test',
                [f"Concept {0}", f"1 - ctg^2(П/6)"],
                "1",
                "4",
                "2",
                "0",
                2
            ],
        ]
    ],
    
]


concepts = [
    [
        "Basic Formulas",
        "Basic Formulas",
        [
            
            "sin^2(a) + cos^2(a) = 1",
            "tg(a) * ctg(a) = 1",
            "tg(a) = sin(a) / cos(a)",
            "ctg(a) = cos(a) / sin(a)",
            "1 + tg^2(a) = 1 / cos^2(a)",
            "1 + ctg^2(a) = 1 / sin^2(a) "            
        ]
    ],
    [
        "Double angle formulas",
        "Double angle formulas",
        [
            "sin(2a) = 2sin(a)cos(a)",
            "cos(2a) = cos^2(a) - sin^2(a)",
            "cos(2a) = 1 - 2sin^2(a)",
            "cos(2a) = 2cos^2(a) - 1",
            "tg(2a) = 2tg(a) / (1 - tg^2(a))",
            "ctg(2a) = ctg^2(a) - 1 / 2ctg(a)"
        ]
    ],
    [
        "Half-argument formulas",
        "Half-argument formulas",
        [
            "sin^2(a/2) = 1 - cos(a) / 2",
            "cos^2(a/2) = 1 + cos(a) / 2",
            "tg^2(a/2) = (1 - cos(a)) / (1 + cos(a))",
            "tg(a/2) = sin(a) / 1 + cos(a)",
            "tg(a/2) = 1 - cos(a) / sin(a)",
            "ctg^2(a/2) = 1 + cos(a) / 1 - cos(a)",
            "ctg(a/2) = sin(a) / 1 - cos(a)",
            "ctg(a/2) = 1 + cos(a) / sin(a)"

        ]
    ],
    [
        "Addition formulas",
        "Addition formulas",
        [
            "sin(a + b) = sin(a)cos(b) + cos(a)sin(b)",
            "cos(a + b) = cos(a)cos(b) - sin(a)sin(b)",
            "tg(a + b) = tg(a) + tg(b) / 1 - tg(a)tg(b)",
            "ctg(a + b) = ctg(a)ctg(b) - 1 / ctg(b) + ctg(a)"
        ]
    ],
    [
        "Subtraction formulas",
        "Subtraction formulas",
        [
            "sin(a - b) = sin(a)cos(b) - cos(a)sin(b)",
            "cos(a - b) = cos(a)cos(b) + sin(a)sin(b)",
            "tg(a + b) = tg(a) - tg(b) / 1 + tg(a)tg(b)",
            "ctg(a + b) = ctg(a)ctg(b) + 1 / ctg(b) - ctg(a)"
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