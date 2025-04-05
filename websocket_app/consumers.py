# import json
# import jwt
# import aiohttp
# from django.conf import settings
# from django.apps import apps
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async

# class LangflowConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         token = self.scope["query_string"].decode().split("=")[-1]

#         user = await self.authenticate_token(token)
#         if user:
#             self.user = user
#             await self.accept()
#         else:
#             await self.close()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data.get("message", "")

#         response = await self.query_langflow(message)

#         await self.send(text_data=json.dumps({"response": response}))

#     async def query_langflow(self, message):
#         """Send message to Langflow API"""
#         async with aiohttp.ClientSession() as session:
#             async with session.post("http://langflow:7860/api/v1/predict", json={"input": message}) as resp:
#                 if resp.status == 200:
#                     result = await resp.json()
#                     return result.get("response", "No response")
#                 return "Langflow error"

#     @database_sync_to_async
#     def authenticate_token(self, token):
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#             User = apps.get_model('auth', 'User')
#             return User.objects.get(id=payload["user_id"])
#         except Exception:
#             return None


import json
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from auth_app.models import CustomUser

class LangflowConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token = self.scope["query_string"].decode().split("=")[-1]

        user = await self.authenticate_token(token)
        if user and user.role == "admin":  # Only admins can connect
            self.user = user
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get("message", "")
        response = await self.process_message(message)
        await self.send(text_data=json.dumps({"response": response}))

    @database_sync_to_async
    def authenticate_token(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return CustomUser.objects.get(id=payload["user_id"])
        except Exception:
            return None

    async def process_message(self, message):
        """Process the incoming message and return a response"""
        # TODO: Implement the logic to process the message and return a response
        return "Message received"


