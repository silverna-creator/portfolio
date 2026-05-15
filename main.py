import flet as ft

def main(page: ft.Page):
    page.title = "My Portfolio"

    page.add(
        ft.Text("Welcome to My Web Portfolio", size=30),
        ft.Text("This is my first website 🚀")
    )

ft.app(target=main)