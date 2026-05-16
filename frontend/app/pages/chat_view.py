import flet as ft
from ..state import AppState, Message
from ..api import ApiClient

def create_chat_view_page(state: AppState, api: ApiClient):
    messages_container = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=8)
    input_field = ft.TextField(hint_text="Сообщение...", expand=True, border=ft.InputBorder.OUTLINE)
    messages = []

    async def load_messages(e):
        nonlocal messages
        if state.active_chat:
            messages = await api.get_messages(state.active_chat.id)
            render_messages()

    def render_messages():
        messages_container.controls.clear()
        for msg in messages:
            is_mine = msg.user_id == state.current_user.id
            bubble = ft.Container(
                content=ft.Text(msg.text, color="white" if is_mine else "black", size=14),
                padding=ft.padding.symmetric(horizontal=12, vertical=8),
                border_radius=12,
                bgcolor=ft.colors.BLUE if is_mine else "grey[200]",
                alignment=ft.alignment.center_right if is_mine else ft.alignment.center_left,
                width=min(280, max(80, len(msg.text) * 8 + 40))
            )
            messages_container.controls.append(bubble)
        messages_container.scroll_to()

    async def send_message(e):
        text = input_field.value.strip()
        if not text or not state.active_chat: return
        msg = await api.send_message(state.active_chat.id, state.current_user.id, text)
        messages.append(msg)
        input_field.value = ""
        render_messages()
        state.refresh()

    header = ft.Container(
        content=ft.Row([
            ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda e: state.navigate_to("/chats"), icon_color="white"),
            ft.Text(state.active_chat.name if state.active_chat else "Чат", size=20, weight="bold", color="white"),
            ft.Container(expand=True)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=ft.padding.symmetric(horizontal=16, vertical=14),
        bgcolor=ft.colors.BLUE,
        border_radius=ft.border_radius.only(top_left=8, top_right=8)
    )

    load_container = ft.Container(content=messages_container, expand=True)#, on_load=load_messages)

    return ft.Column(
        controls=[
            header,
            ft.Container(content=load_container, expand=True, border=ft.border.all(1, "grey[300]"), border_radius=8),
            ft.Row(controls=[input_field, ft.IconButton(ft.icons.SEND, on_click=send_message)])
        ], expand=True
    )