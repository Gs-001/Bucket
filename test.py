import flet
from flet import Checkbox, ElevatedButton, Row, Text, TextField, Column
from flet import (
    AppBar,
    Icon,
    IconButton,
    Page,
    PopupMenuButton,
    PopupMenuItem, Text,
    colors,
    icons,
    View
)


def main(page: Page):
    page.scroll = 'always'

    def change_route(route):

        new_task = TextField(hint_text="Whats needs to be done?", width=300)
        first_name = TextField(disabled=True)
        last_name = TextField(disabled=True)
        first_name.disabled = True
        last_name.disabled = True

        c = Column(
            controls=[
                first_name,
                last_name,
            ],
            disabled=True,
        )

        t = Text(
            value="This is a Text control sample",
            size=30,
            color="white",
            bgcolor="pink",
            weight="bold",
            italic=True,)

        def add_clicked(e):
            page.add(Checkbox(label=new_task.value))

        def check_item_clicked(e):
            e.control.checked = not e.control.checked
            page.update()

        page.views.clear()  # CLEAR THE VIEWS
        page.views.append(  # BUILD THE VIEW 1
            View(
                route='/',
                controls=[
                    AppBar(
                        title=Text(f"Main route ({page.route})"),
                        bgcolor=colors.SURFACE_VARIANT
                    ),
                    ElevatedButton("Go to another view",
                                   on_click=lambda _: page.go("/another_view")),
                    t,
                    c,
                    Row([new_task, ElevatedButton("Add", on_click=add_clicked)])

                ]
            )
        )
        if page.route == "/another_view":
            page.views.append(  # BUILD THE VIEW 2
                View(
                    route='/another_view',
                    controls=[
                        AppBar(
                            title=Text(f"Other view ({page.route})"),
                            leading=Icon(icons.PALETTE),
                            leading_width=40,
                            center_title=False,
                            bgcolor=colors.SURFACE_VARIANT,
                            actions=[
                                IconButton(icons.WB_SUNNY_OUTLINED),
                                IconButton(icons.FILTER_3),
                                PopupMenuButton(
                                    items=[
                                        PopupMenuItem(text="Item 1"),
                                        PopupMenuItem(),  # divider
                                        PopupMenuItem(
                                            text="Checked item", checked=False, on_click=check_item_clicked
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        ElevatedButton("Go to main view",
                                       on_click=lambda _: page.go("/")),
                        Text("Body!")
                    ]
                )
            )

        page.update()

    page.on_route_change = change_route
    page.go(page.route)


flet.app(target=main)
