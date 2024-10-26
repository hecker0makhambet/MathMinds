import flet as ft

from variables1 import tasks
from variables1 import concepts

elem = ft.Text("ABOBA")

username = "Makhambet"

concepts_status = 0
homepage_status = 0
current_task = 0
current_topic = 0
score = 0
errors = 0


def main(page: ft.Page):
    page.title = "MathMinds"
    page.bgcolor = ft.colors.with_opacity(1, "#B39DF2")
    page.fonts = {
        "Aclonica": "data\\Aclonica-Regular.ttf",
    }
    page.window_width = 390
    page.window_height = 750
    # page.window_resizable = False
    
    page.padding = 0

    def change_homepage(e):
        homepage.visible = homepage_status % 2 == 0
        conceptspage.visible = False
        conceptspagenext.visible = False
        taskspage.visible = homepage_status % 2 == 1
        profilepage.visible = False
        # page.controls = [homepage, conceptspage, conceptspagenext, taskspage, profilepage]
        page.update()

    def change_conceptspage(e):
        global concepts_status
        homepage.visible = False
        conceptspage.visible = concepts_status % 2 == 0
        conceptspagenext.visible = concepts_status % 2 == 1
        taskspage.visible = False
        profilepage.visible = False
        page.update()

    def change_profilepage(e):
        homepage.visible = False
        conceptspage.visible = False
        conceptspagenext.visible = False
        taskspage.visible = False
        profilepage.visible = True
        update_profile()
        page.update()

    def update_profile():
        if score / len(tasks) >= 0.5:
            # text_percentage = ft.Text(
            #     f"{round(score / len(tasks), 1)}%",
            #     font_family="Aclonica",
            #     color=ft.colors.with_opacity(1, "#F0ECFB"),
            #     size=24
            # )
            # text_concept = ft.Text(
            #     f"{concepts[i][0]}",
            #     font_family="Aclonica",
            #     color=ft.colors.with_opacity(1, "#F0ECFB"),
            #     size=24
            # )
            progress_bars = ft.Column(
                [
                    ft.Row(
                        [
                            ft.Stack(
                                [
                                    ft.Container(
                                        ft.Text(
                                            f"{round(score / len(tasks) * 100)}%",
                                            font_family="Aclonica",
                                            color=ft.colors.with_opacity(1, "#000000"),
                                            size=24
                                        ),
                                        width=328,
                                        height=70,
                                        bgcolor=ft.colors.with_opacity(1, "#D9D9D9"),
                                        border_radius=15,
                                        alignment=ft.alignment.center_right,
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            f"{concepts[i][0]}",
                                            font_family="Aclonica",
                                            color=ft.colors.with_opacity(1, "#F0ECFB"),
                                            size=24
                                        ),
                                        width=328 * (score / len(tasks)),
                                        height=70,
                                        bgcolor=ft.colors.with_opacity(1, "#825EEB"),  # Violet
                                        border_radius=15,
                                        alignment=ft.alignment.center
                                    )
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                    for i in range(len(concepts))
                ]
            )
        else:
            progress_bars = ft.Column(
                [
                    ft.Row(
                        [
                            ft.Stack(
                                [
                                    ft.Container(
                                        ft.Text(
                                            f"{concepts[i][0]}",
                                            font_family="Aclonica",
                                            color=ft.colors.with_opacity(1, "#000000"),
                                            size=24
                                        ),
                                        width=328,
                                        height=70,
                                        bgcolor=ft.colors.with_opacity(1, "#D9D9D9"),
                                        border_radius=15,
                                        alignment=ft.alignment.center_right,
                                    ),
                                    ft.Container(
                                        ft.Text(
                                            f"{round(score / len(tasks) * 100, 1)}%",
                                            font_family="Aclonica",
                                            color=ft.colors.with_opacity(1, "#F0ECFB"),  # Violet
                                            size=24
                                        ),
                                        width=328 * ((score) / len(tasks)),
                                        height=70,
                                        bgcolor=ft.colors.with_opacity(1, "#825EEB"),
                                        border_radius=15,
                                        alignment=ft.alignment.center
                                    )
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                    for i in range(len(concepts))
                ]
            )
        profilepage.controls[-1].controls[-1] = progress_bars

    def changing_pages(e):
        road_map = {
            0: change_homepage,
            1: change_conceptspage,
            2: change_profilepage
        }
        road_map[e.control.selected_index](e)

    def correct_choice(e):
        global score_label
        global current_task
        global current_topic
        global score
        score += 1
        score_label.content = ft.Text(
            f"Score: {score}",
            font_family="Aclonica"
        )
        current_task += 1
        current_task %= len(tasks[current_topic][1])
        if current_task == 0:
            current_topic += 1
            current_topic %= len(tasks)
            if current_topic == 0:
                open_close_tasks(e, 0, topics_closed=True)
            else:    
                open_close_tasks(e, 0, topic_closed=True)
        else:
            open_close_tasks(e, 0)
        page.update()

    def wrong_choice(e):
        global errors
        errors += 1
        errors_label.controls = [
            ft.Text(
                f"Errors: {errors}",
                font_family="Aclonica"
            )
        ]
        page.update()

    def choose_answer(e, ans):
        if ans == tasks[current_topic][1][current_task][-1]:
            page.dialog = ft.AlertDialog(
                content=ft.Text(
                    "Correct!",
                    font_family="Aclonica"
                ),
                on_dismiss=correct_choice,
                open=True
            )
            page.update()
        else:
            page.dialog = ft.AlertDialog(
                content=ft.Text(
                    "Incorrect! Try again!",
                    font_family="Aclonica"
                ),
                on_dismiss=wrong_choice,
                open=True
            )
            page.update()

    def change_answer_text(e):
        global answer_text
        answer_text = e.control.value

    def return_text_task():
        tasks_view = ft.Container(
            ft.Row(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    ft.ElevatedButton(
                                        "Get back to home",
                                        on_click=lambda e: open_close_tasks(e, 1),
                                    )
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"{tasks[current_topic][1][current_task][1][0]}",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=36
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"{tasks[current_topic][1][current_task][1][1]}",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=24
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.TextField(
                                        label="Your answer",
                                        on_change=change_answer_text,
                                    )
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                f"Submit",
                                                on_click=lambda e: choose_answer(e, answer_text),
                                                width=210,
                                                height=40,
                                                style=ft.ButtonStyle(
                                                    color={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        
                                                    },
                                                    bgcolor={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(0.8, "#B7B3C1"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(0.8, "#F0ECFB"),
                                                    },
                                                    padding={ft.MaterialState.HOVERED: 20},
                                                    overlay_color=ft.colors.TRANSPARENT,
                                                    elevation={"pressed": 0, "": 1},
                                                    animation_duration=1000,
                                                    # side={
                                                    #     ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                                                    #     ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                                                    # },
                                                    shape={
                                                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                                                    },
                                                )
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                                    
                                )
                            ]
                        ),
                        width=328,
                        height=576,
                        bgcolor=ft.colors.with_opacity(0.9, "#825EEB"),
                        border_radius=15,
                        margin=ft.margin.only(top=100),
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        return tasks_view

    def return_test_task():
        tasks_view = ft.Container(
            ft.Row(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    ft.ElevatedButton(
                                        "Get back to home",
                                        on_click=lambda e: open_close_tasks(e, 1),
                                    )
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"{tasks[current_topic][1][current_task][1][0]}",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=36
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"{tasks[current_topic][1][current_task][1][1]}",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=24
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                f"{tasks[current_topic][1][current_task][2]}",
                                                on_click=lambda e: choose_answer(e, 1),
                                                width=210,
                                                height=40,
                                                style=ft.ButtonStyle(
                                                    color={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        
                                                    },
                                                    bgcolor={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(0.8, "#B7B3C1"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(0.8, "#F0ECFB"),
                                                    },
                                                    padding={ft.MaterialState.HOVERED: 20},
                                                    overlay_color=ft.colors.TRANSPARENT,
                                                    elevation={"pressed": 0, "": 1},
                                                    animation_duration=1000,
                                                    # side={
                                                    #     ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                                                    #     ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                                                    # },
                                                    shape={
                                                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                                                    },
                                                )
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                                    
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                f"{tasks[current_topic][1][current_task][3]}",
                                                on_click=lambda e: choose_answer(e, 2),
                                                width=210,
                                                height=40,
                                                style=ft.ButtonStyle(
                                                    color={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        
                                                    },
                                                    bgcolor={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(0.8, "#B7B3C1"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(0.8, "#F0ECFB"),
                                                    },
                                                    padding={ft.MaterialState.HOVERED: 20},
                                                    overlay_color=ft.colors.TRANSPARENT,
                                                    elevation={"pressed": 0, "": 1},
                                                    animation_duration=1000,
                                                    # side={
                                                    #     ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                                                    #     ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                                                    # },
                                                    shape={
                                                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                                                    },
                                                )
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                                    
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                f"{tasks[current_topic][1][current_task][4]}",
                                                on_click=lambda e: choose_answer(e, 3),
                                                width=210,
                                                height=40,
                                                style=ft.ButtonStyle(
                                                    color={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        
                                                    },
                                                    bgcolor={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(0.8, "#B7B3C1"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(0.8, "#F0ECFB"),
                                                    },
                                                    padding={ft.MaterialState.HOVERED: 20},
                                                    overlay_color=ft.colors.TRANSPARENT,
                                                    elevation={"pressed": 0, "": 1},
                                                    animation_duration=1000,
                                                    # side={
                                                    #     ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                                                    #     ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                                                    # },
                                                    shape={
                                                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                                                    },
                                                )
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                                    
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                f"{tasks[current_topic][1][current_task][5]}",
                                                on_click=lambda e: choose_answer(e, 4),
                                                width=210,
                                                height=40,
                                                style=ft.ButtonStyle(
                                                    color={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        
                                                    },
                                                    bgcolor={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(0.8, "#B7B3C1"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(0.8, "#F0ECFB"),
                                                    },
                                                    padding={ft.MaterialState.HOVERED: 20},
                                                    overlay_color=ft.colors.TRANSPARENT,
                                                    elevation={"pressed": 0, "": 1},
                                                    animation_duration=1000,
                                                    # side={
                                                    #     ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                                                    #     ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                                                    # },
                                                    shape={
                                                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                                                    },
                                                )
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                                    
                                ),
                            ]
                        ),
                        width=328,
                        height=576,
                        bgcolor=ft.colors.with_opacity(0.9, "#825EEB"),
                        border_radius=15,
                        margin=ft.margin.only(top=100),
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        return tasks_view

    def return_matching_task():
        pass

    def return_topic_closed_message():
        message = ft.Container(
            ft.Row(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    ft.ElevatedButton(
                                        "Get back to home",
                                        on_click=lambda e: open_close_tasks(e, 1),
                                    )
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"You succesfully finished the topic {tasks[current_topic - 1][0]}",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=36
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"Now turn to the Concepts page to study new topic",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=24
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                f"OK",
                                                on_click=lambda e: open_close_tasks(e, 1),
                                                width=210,
                                                height=40,
                                                style=ft.ButtonStyle(
                                                    color={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        
                                                    },
                                                    bgcolor={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(0.8, "#B7B3C1"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(0.8, "#F0ECFB"),
                                                    },
                                                    padding={ft.MaterialState.HOVERED: 20},
                                                    overlay_color=ft.colors.TRANSPARENT,
                                                    elevation={"pressed": 0, "": 1},
                                                    animation_duration=1000,
                                                    # side={
                                                    #     ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                                                    #     ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                                                    # },
                                                    shape={
                                                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                                                    },
                                                )
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                                    
                                )
                            ]
                        ),
                        width=328,
                        height=576,
                        bgcolor=ft.colors.with_opacity(0.9, "#825EEB"),
                        border_radius=15,
                        margin=ft.margin.only(top=100),
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        return message

    def return_all_topics_closed_message():
        message = ft.Container(
            ft.Row(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    ft.ElevatedButton(
                                        "Get back to home",
                                        on_click=lambda e: open_close_tasks(e, 1),
                                    )
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"Congratulations! You succesfully completed the entire course of MathMinds program",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=24
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"We regularly update our topics so that you could improve your math knowledge",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=24
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Text(
                                        f"We will keep in touch soon",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#FFFFFF"),
                                        size=24
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                f"OK",
                                                on_click=lambda e: open_close_tasks(e, 1),
                                                width=210,
                                                height=40,
                                                style=ft.ButtonStyle(
                                                    color={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(1, "#FFFFFF"),
                                                        
                                                    },
                                                    bgcolor={
                                                        ft.MaterialState.HOVERED: ft.colors.with_opacity(0.8, "#B7B3C1"),
                                                        ft.MaterialState.DEFAULT: ft.colors.with_opacity(0.8, "#F0ECFB"),
                                                    },
                                                    padding={ft.MaterialState.HOVERED: 20},
                                                    overlay_color=ft.colors.TRANSPARENT,
                                                    elevation={"pressed": 0, "": 1},
                                                    animation_duration=1000,
                                                    # side={
                                                    #     ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                                                    #     ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                                                    # },
                                                    shape={
                                                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                                                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                                                    },
                                                )
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )
                                    
                                )
                            ]
                        ),
                        width=328,
                        height=576,
                        bgcolor=ft.colors.with_opacity(0.9, "#825EEB"),
                        border_radius=15,
                        margin=ft.margin.only(top=100),
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        return message
    
    def open_close_tasks(e, num, topic_closed=False, topics_closed=False):
        global homepage_status
        homepage_status += num
        if topics_closed:
            taskspage.controls[-1] = return_all_topics_closed_message()
        elif topic_closed:
            taskspage.controls[-1] = return_topic_closed_message()
        elif tasks[current_topic][1][current_task][0] == 'test':
            taskspage.controls[-1] = return_test_task()
        elif tasks[current_topic][1][current_task][0] == 'text':
            taskspage.controls[-1] = return_text_task()
            
        change_homepage(e)

    def open_close_concepts(e):
        global concepts_status
        concepts_status += 1
        change_conceptspage(e)

    def return_concept_cards(concept):
        return [
            ft.Row(
                [
                    ft.Container(
                        ft.Text(
                            f"{concepts[concept][2][i]}",
                            font_family="Aclonica",
                            color=ft.colors.with_opacity(1, "#F0ECFB")
                        ),
                        width=241,
                        height=40,
                        border_radius=7,
                        bgcolor=ft.colors.with_opacity(1, "#BBA8F3"),
                        alignment=ft.alignment.center
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ) for i in range(len(concepts[concept][2]))
        ]

    def open_new_concept(e, concept):
        concept_view = ft.Container(
            ft.Row(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text(
                                            f"{concepts[concept][0]}",
                                            size=36,
                                            font_family="Aclonica",
                                            color=ft.colors.with_opacity(1, "#F0ECFB"),
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    [
                                        ft.Text(
                                            f"{concepts[concept][1]}",
                                            font_family="Aclonica",
                                            color=ft.colors.with_opacity(1, "#F0ECFB"),
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                # ft.Text(
                                #     f"Concept {num} is a concept about {num}",
                                #     font_family="Aclonica",
                                # ),
                                # ft.Text(
                                #     f"{num}",
                                #     font_family="Aclonica"
                                # )
                            ] + return_concept_cards(concept)
                        ),
                        # left=21,
                        # top=108,
                        height=576,
                        width=328,
                        bgcolor=ft.colors.with_opacity(0.9, "#825EEB"),
                        border_radius=15
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            margin=ft.margin.only(top=120)
        )
        conceptspagenext.controls.append(
            concept_view
        )
        open_close_concepts(e)

    def close_concept(e):
        conceptspagenext.controls.pop(-1)
        open_close_concepts(e)

    def return_concept_button(concept):
        return ft.Container(
                ft.ElevatedButton(
                    content=ft.Text(
                        f"{concepts[concept][0]}",
                        font_family="Aclonica"
                    ),
                    on_click=lambda e: open_new_concept(e, concept),
                    width=328,
                    height=88,
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.HOVERED: ft.colors.WHITE,
                            ft.MaterialState.DEFAULT: ft.colors.with_opacity(1, "#F0ECFB"),
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.with_opacity(1, "#6F56BB"),
                            "": ft.colors.with_opacity(0.9, "#8765EC")
                        },
                        padding={ft.MaterialState.HOVERED: 20},
                        overlay_color=ft.colors.TRANSPARENT,
                        elevation={"pressed": 0, "": 1},
                        animation_duration=500,
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                            ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                        },
                        shape={
                            ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=15),
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
                        },
                    ),

                ),
            ) 


    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.colors.AMBER_100,
        inactive_color=ft.colors.GREY,
        active_color=ft.colors.BLACK,
        # on_change=lambda e: print("Selected tab:", e.control.selected_index),
        on_change=changing_pages,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME_OUTLINED,
                selected_icon=ft.icons.HOME_ROUNDED,
                label="Home",
            ),
            ft.NavigationDestination(icon=ft.icons.MENU_BOOK_OUTLINED, label="Concepts"),
            ft.NavigationDestination(
                icon=ft.icons.PERSON_OUTLINE_ROUNDED,
                selected_icon=ft.icons.PERSON,
                label="Profile",
            ),
        ]
    )

    homepage = ft.Stack(
        [
            ft.Column(
                [
                    # ft.ResponsiveRow(
                    #     [
                    #         ft.Column(
                    #             [
                    #                 ft.Row(
                    #                     [
                    #                         ft.Text(
                    #                             "MathMinds",
                    #                             font_family='Aclonica',
                    #                             size=38,
                    #                             color=ft.colors.with_opacity(1, "#F0ECFB"),
                    #                         ),
                    #                     ],
                    #                     alignment=ft.MainAxisAlignment.CENTER,
                    #                 ),
                    #             ]
                    #         )
                    #     ],
                    #     # alignment=ft.MainAxisAlignment.CENTER,
                    # ),
                    ft.Row(
                        [
                            ft.Image(
                                src="data\\mainpage.png",
                                height=554
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.ElevatedButton(
                                    text="START",
                                    on_click=lambda e: open_close_tasks(e, 1)
                                ),
                                margin=50
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
            
        ],
        width=page.window_max_width,
        height=page.window_max_height,
    )
    global score_label
    score_label = ft.Container(
            ft.Text(
            f"Score: {score}",
            font_family="Aclonica"
        )
    )

    global errors_label
    errors_label = ft.Row(
        [
            ft.Text(
                f"Errors: {errors}",
                font_family="Aclonica"
            ),
        ],
        alignment=ft.MainAxisAlignment.END
    )
    
    taskspage = ft.Stack(
        [
            ft.Container(
                ft.ResponsiveRow(
                    [
                        ft.Row(
                            [
                                ft.Text(
                                    "Concepts",
                                    font_family="Aclonica",
                                    size=36,
                                    color=ft.colors.with_opacity(1, "#F0ECFB"),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                ),
            ),
            score_label,
            errors_label,
            ft.Text(""),
        ],
        visible=False,
        width=page.window_max_width,
        height=page.window_max_height,
    )
    concept_buttons = [
        return_concept_button(i) for i in range(len(concepts))
    ] 

    conceptspage = ft.Stack(
        [
            ft.Container(
                ft.ResponsiveRow(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    ft.Text(
                                        "Concepts",
                                        font_family="Aclonica",
                                        color=ft.colors.with_opacity(1, "#F0ECFB"),
                                        size=36
                                    )
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]
                )
            ),
            ft.Container(
                ft.ResponsiveRow(
                    [
                        ft.Row(
                            [
                                ft.Column(
                                    concept_buttons
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ]
                ),
                margin=ft.margin.only(top=100),
            )
            
        ],
        visible=False,
        width=page.window_max_width,
        height=page.window_max_height,
    )
    conceptspagenext = ft.Stack(
        [
            ft.Container(
                ft.ElevatedButton(
                    "GET BACK TO CONCEPTS",
                    on_click=close_concept,
                )
            ),
            ft.Container(
                ft.ResponsiveRow(
                    [
                        ft.Row(
                            [
                                ft.Text(
                                    "Concepts",
                                    font_family="Aclonica",
                                    color=ft.colors.with_opacity(1, "#F0ECFB"),
                                    size=42
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ]
                ),
                margin=ft.margin.only(top=50)
            )

        ],
        visible=False,
        width=page.window_max_width,
        height=page.window_max_height,
    )
    profilepage = ft.Stack(
        [
            ft.Container(
                width=page.window_max_width,
                height=166,
                bgcolor=ft.colors.with_opacity(1, "#825EEB"),
                margin=0,
                border_radius=ft.BorderRadius(bottom_right=15, bottom_left=15, top_right=0, top_left=0)
            ),
            ft.Column(
                [
                    ft.ResponsiveRow(
                        [
                            ft.Row(
                                [
                                    ft.Text(
                                        "Profile",
                                        font_family="Aclonica",
                                        size=30,
                                        color=ft.colors.with_opacity(1, "#F0ECFB")
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                        ],
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.Image(
                                    src="data\\icon_user.png",
                                    width=200,
                                    height=200,
                                    border_radius=100,
                                ),
                                # ft.Text(""),
                                width=200,
                                height=200,
                                border_radius=100,
                                margin=ft.margin.only(top=36),
                                bgcolor=ft.colors.with_opacity(1, "#D9D9D9"),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                ft.Text(
                                    f"{username}",
                                    font_family="Aclonica",
                                    size=25,
                                    color=ft.colors.with_opacity(1, "#F0ECFB"),
                                    text_align=ft.MainAxisAlignment.CENTER
                                ),
                                alignment=ft.alignment.center
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.Stack(
                                [
                                    ft.Container(
                                        ft.Text(
                                            f"{score / len(tasks) * 100}%",
                                            font_family="Aclonica",
                                            color=ft.colors.with_opacity(1, "#F0ECFB"),
                                            size=24
                                        ),
                                        width=328,
                                        height=70,
                                        bgcolor=ft.colors.with_opacity(1, "#D9D9D9"),
                                        border_radius=15,
                                        alignment=ft.alignment.center,
                                    ),
                                    ft.Container(
                                        # ft.Text(
                                        #     f"{score / len(tasks) * 100}%",
                                        #     font_family="Aclonica",
                                        #     color=ft.colors.with_opacity(1, "#F0ECFB"),
                                        #     size=24
                                        # ),
                                        ft.Text(''),
                                        width=328 * (score / len(tasks)),
                                        height=70,
                                        bgcolor=ft.colors.with_opacity(1, "#825EEB"),
                                        border_radius=15,
                                        alignment=ft.alignment.center
                                    )
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ]
            ),
            # ft.ResponsiveRow(
            #     [
            #         ft.Column
            #     ]
            # )
        ],
        visible=False,
        width=page.window_max_width,
        height=page.window_max_height,
    )

    page.add(homepage, conceptspage, conceptspagenext, taskspage, profilepage)
    page.update()


ft.app(target=main)