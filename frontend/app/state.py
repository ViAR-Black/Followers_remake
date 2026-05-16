from dataclasses import dataclass, field
from typing import Optional, List, Dict

@dataclass
class User:
    id: int
    username: str

@dataclass
class Chat:
    id: int
    name: str
    type: str # general, private, group

@dataclass
class Message:
    id: int
    chat_id: int
    user_id: int
    text: str
    timestamp: str

class AppState:
    def __init__(self):
        self.current_user: Optional[User] = None
        self.active_chat: Optional[Chat] = None
        self.chats: List[Chat] = []
        self.page = None # link on flet.Page

    def set_page(self, page):
        self.page = page

    def navigate_to(self, route: str):
        if self.page:
            self.page.go(route)

    def refresh(self):
        if self.page:
            self.page.update()