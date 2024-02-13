import flet as ft

from variables import tasks
from variables import concepts

elem = ft.Text("ABOBA")

username = "Makhambet"

concepts_status = 0
homepage_status = 0
current_task = 0


def main(page: ft.Page):
    page.title = "MathMinds"
    page.bgcolor = ft.colors.with_opacity(1, "#B39DF2")
    page.fonts = {
        "Aclonica": "data\\Aclonica-Regular.ttf",
    }
    page.window_width = 390
    page.window_height = 844
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
        page.update()

    def changing_pages(e):
        road_map = {
            0: change_homepage,
            1: change_conceptspage,
            2: change_profilepage
        }
        road_map[e.control.selected_index](e)

    def correct_choice(e):
        global current_task
        current_task += 1
        current_task %= len(tasks)
        page.update()

    def wrong_choice(e):
        pass

    def choose_answer(e, ans):
        if ans == tasks[current_task][5]:
            page.dialog = ft.AlertDialog(
                content=ft.Text(
                    "VERY GOOD",
                    font_family="Aclonica"
                ),
                on_dismiss=correct_choice,
                open=True
            )
            page.update()
        else:
            page.dialog = ft.AlertDialog(
                content=ft.Text(
                    "NOT SO GOOD",
                    font_family="Aclonica"
                ),
                on_dismiss=wrong_choice,
                open=True
            )
            page.update()

    def open_close_tasks(e):
        global homepage_status
        homepage_status += 1
        if homepage_status % 2 == 0:
            taskspage.controls.pop(-1)
        else:
            taskspage.controls.append(
                ft.Container(
                    ft.Row(
                        [
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Container(
                                            ft.ElevatedButton(
                                                "Get back to home",
                                                on_click=open_close_tasks,
                                            )
                                        ),
                                        ft.Container(
                                            ft.Text(
                                                f"{tasks[current_task][0][0]}",
                                                font_family="Aclonica",
                                                color=ft.colors.with_opacity(1, "#FFFFFF"),
                                                size=36
                                            ),
                                            alignment=ft.alignment.center
                                        ),
                                        ft.Container(
                                            ft.Text(
                                                f"{tasks[current_task][0][1]}",
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
                                                        f"{tasks[current_task][1]}",
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
                                                        f"{tasks[current_task][2]}",
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
                                                        f"{tasks[current_task][3]}",
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
                                                        f"{tasks[current_task][4]}",
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
             
            )
            
        change_homepage(e)

    def open_close_concepts(e):
        global concepts_status
        concepts_status += 1
        change_conceptspage(e)

    def open_new_concept(e, num):
        conceptspagenext.controls.append(
            ft.Container(
                ft.Row(
                    [
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(
                                                f"{concepts[num][0]}",
                                                size=36,
                                                font_family="Aclonica",
                                                color=ft.colors.with_opacity(1, "#F0ECFB")
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Text(
                                                f"{concepts[num][1]}",
                                                font_family="Aclonica",
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Container(
                                                ft.Text(
                                                    f"{concepts[num][2]}",
                                                    font_family="Aclonica"
                                                ),
                                                width=241,
                                                height=40,
                                                border_radius=7,
                                                bgcolor=ft.colors.with_opacity(1, "#BBA8F3"),
                                                alignment=ft.alignment.center
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    ft.Text(
                                        f"{concepts[num][2]}",
                                        font_family="Aclonica",
                                    )
                                    # ft.Text(
                                    #     f"Concept {num} is a concept about {num}",
                                    #     font_family="Aclonica",
                                    # ),
                                    # ft.Text(
                                    #     f"{num}",
                                    #     font_family="Aclonica"
                                    # )
                                ]
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
            
            # ft.Container(
            #     ft.Text(
            #         f"Concept {num} is a concept about ABOBA",
            #     ),
            #     margin=100,
            # )
        )
        open_close_concepts(e)

    def close_concept(e):
        conceptspagenext.controls.pop(-1)
        open_close_concepts(e)

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
            ft.ResponsiveRow(
                [
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text(
                                        "MathMinds",
                                        font_family='Aclonica',
                                        size=38,
                                        color=ft.colors.with_opacity(1, "#F0ECFB"),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ]
                    )
                ],
                # alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(
                ft.ElevatedButton(
                    text="START",
                    on_click=open_close_tasks
                ),
                margin=100
            ),
        ],
        width=page.window_max_width,
        height=page.window_max_height,
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
            )
        ],
        visible=False,
        width=page.window_max_width,
        height=page.window_max_height,
    )
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
                                    [
                                        ft.Container(
                                            ft.ElevatedButton(
                                                content=ft.Text(
                                                    "CONCEPT1",
                                                    font_family="Aclonica"
                                                ),
                                                on_click=lambda e: open_new_concept(e, 1),
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
                                        ),
                                        ft.Container(
                                            ft.ElevatedButton(
                                                content=ft.Text(
                                                    "CONCEPT2",
                                                    font_family="Aclonica"
                                                ),
                                                # "CONCEPT2",
                                                on_click=lambda e: open_new_concept(e, 2),
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
                                        ),
                                    ]
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
                    ft.Column(
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
                            ),
                            ft.Container(
                                ft.Text(
                                    f"{username}",
                                    font_family="Aclonica",
                                    size=25,
                                    color=ft.colors.with_opacity(1, "#F0ECFB")
                                ),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            
        ],
        visible=False,
        width=page.window_max_width,
        height=page.window_max_height,
    )

    page.add(homepage, conceptspage, conceptspagenext, taskspage, profilepage)
    page.update()


ft.app(target=main)