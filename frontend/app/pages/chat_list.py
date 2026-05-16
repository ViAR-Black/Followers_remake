import flet as ft
from ..state import AppState, Chat

def create_chat_list_page(state: AppState):
    list_view = ft.ListView(spacing=4, padding=10, expand=True)

    def _open_chat(chat: Chat):
        state.active_chat = chat
        state.navigate_to("/chat")

    def render():
        list_view.controls.clear()
        for chat in state.chats:
            tile = ft.ListTile(
                leading=ft.Icon(ft.icons.CHAT, color=ft.colors.BLUE),
                title=ft.Text(chat.name, weight="bold"),
                subtitle=ft.Text(f"Тип: {chat.type}", size=12, color="grey"),
                trailing=ft.Icon(ft.icons.ARROW_FORWARD, size=16)
            )
            tile.on_click = lambda e, c=chat: _open_chat(c)
            list_view.controls.append(tile)
        state.refresh()

    render()

    header = ft.Container(
        content=ft.Row([
            ft.Text("Мессенджер", size=22, weight="bold", color="white"),
            ft.Icon(ft.icons.PERSON, color="white", size=28)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.padding.symmetric(horizontal=16, vertical=14),
        bgcolor=ft.colors.BLUE,
        border_radius=ft.border_radius.only(top_left=8, top_right=8)
    )

    return ft.Column(
        controls=[header, ft.Text("Выберите чат:", size=14), list_view],
        expand=True
    )