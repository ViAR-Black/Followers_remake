import flet as ft
from frontend.app.state import AppState
from frontend.app.api import ApiClient

def create_login_page(state: AppState, api: ApiClient):
    username = ft.TextField(label='Login', width=300)
    password = ft.TextField(label='Password', password=True, width=300)
    error_text = ft.Text('', color='red', size='14')
    btn = ft.ElevatedButton('Войти', width=300)

    async def on_login(e):
        btn.disabled = True
        error_text.value = ""
        state.refresh()
        try:
            user = await api.login(username.value, password.value)
            state.current_user = user
            state.chats = await api.get_chats(user.id)
            state.navigate_to('/chats')
        except Exception as ex:
            error_text.value = str(ex)
        finally:
            btn.disabled = False
            state.refresh()

    btn.on_click = on_login

    return ft.Column(
        controls=[ft.Text('Sing in', size=28, weight='bold'), ft.Divider(),
                  username, password, error_text, btn],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15, expand=True
    )