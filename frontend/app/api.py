# Клиент
# Сейчас мок, позже заменим на http/ws

import asyncio
from typing import List
from .state import User, Chat, Message

class ApiClient:
    def __init__(self):
        self._mock_users = {1: User(1, 'test'), 2: User(2, 'ViAR')}
        self._mock_chats = [
            Chat(1, 'General chat', 'general'),
            Chat(2, "Private: test <-> ViAR", 'private'),
            Chat(3, 'The project Alpha', 'group')
        ]
        self._mock_messages = {
            1: [Message(1, 1, 2, 'Hi, whats up?', '2026-05-16 10:00')],
            2: [], 3: []
        }

    async def login(self, username: str, password: str) -> User: # позже заменить на pydantic
        await asyncio.sleep(0.3)
        if username == 'test' and password == 'test':
            return self._mock_users[1]
        raise ValueError('Uncorrect login or password')
    
    async def get_chats(self, user_id: int):
        await asyncio.sleep(0.2)
        return self._mock_chats
    
    async def get_messages(self, chat_id: int) -> List[Message]:
        await asyncio.sleep(0.2)
        return self._mock_messages.get(chat_id, [])
    
    async def send_message(self, chat_id: int, user_id: int, text: str) -> Message:
        await asyncio.sleep(0.1)
        msg = Message(len(self._mock_messages.get(chat_id, [])) + 1, chat_id, user_id, text, '2026-05-16 10:05')
        self._mock_messages.setdefault(chat_id, []).append(msg)
        return msg