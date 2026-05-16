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
                leading=ft.Icon('chat', color='blue'),
                title=ft.Text(chat.name, weight="bold"),
                subtitle=ft.Text(f"Тип: {chat.type}", size=12, color="grey"),
                trailing=ft.Icon('arrow_forward', size=16)
            )
            tile.on_click = lambda e, c=chat: _open_chat(c)
            list_view.controls.append(tile)
        state.refresh()

    render()

    header = ft.Container(
        content=ft.Row([
            ft.Text("Мессенджер", size=22, weight="bold", color="white"),
            ft.Icon('person', color="white", size=28)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.Padding.symmetric(horizontal=16, vertical=14),
        bgcolor='blue',
        border_radius=ft.BorderRadius.only(top_left=8, top_right=8, bottom_left=0, bottom_right=0)
    )

    return ft.Column(
        controls=[header, ft.Text("Выберите чат:", size=14), list_view],
        expand=True
    )