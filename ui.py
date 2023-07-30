import flet as ft
# from utils import create_transaction

def create_transaction(e):
    print("Create Transaction")

def main(page: ft.Page):

    floating_action_button = ft.FloatingActionButton(
        content=ft.Row(
            [ft.Icon(ft.icons.ADD), ft.Text("Add Transaction")], alignment="center", spacing=5
        ),
        bgcolor=ft.colors.AMBER_300,
        shape=ft.RoundedRectangleBorder(radius=5),
        width=300,
        mini=True,
        on_click=create_transaction
    )

    create_txn_view = ft.Column(
        controls=[
            ft.TextField(hint_text="Title"),
            ft.TextField(hint_text="Amount"),
            ft.Dropdown(
                width=100,
                options=[
                    ft.dropdown.Option("Red"),
                    ft.dropdown.Option("Green"),
                    ft.dropdown.Option("Blue"),
                ],
            )
        ])

    def change_route(route):
        if page.route == "/add_txn":
            page.views.append(create_txn_view)
        

    page.add(ft.Text("Just a text!"), floating_action_button)


ft.app(target=main)
