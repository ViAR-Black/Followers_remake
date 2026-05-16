import flet as ft
from .state import AppState
from .api import ApiClient
from .pages import login, chat_list, chat_view

def main(page: ft.Page):
    page.title = 'Followers'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 420
    page.window.height = 750
    page.window.resizable = False

    state = AppState()
    state.set_page(page)
    api = ApiClient()

    def on_route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        view = ft.View(padding=0)

        if page.route == '/chats':
            view.controls.append(chat_list.create_chat_list_page(state))
        elif page.route == '/chat':
            view.controls.append(chat_view.create_chat_view_page(state, api))
        else:
            view.controls.append(login.create_login_page(state, api))

        page.views.append(view)
        page.update()

    page.on_route_change = on_route_change
    page.go('/')

if __name__ == '__main__':
    ft.app(target=main)