# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            logger.info(f"WebSocket connection attempt from {self.scope['client']}")
            
            self.room_group_name = 'notifications'
            
            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            
            await self.accept()
            logger.info(f"WebSocket connection accepted for {self.channel_name}")
            
            # Send welcome message
            await self.send(text_data=json.dumps({
                'message': 'Connected to notification service'
            }))
        except Exception as e:
            logger.error(f"Error in WebSocket connect: {str(e)}", exc_info=True)
            raise

    async def disconnect(self, close_code):
        try:
            logger.info(f"WebSocket disconnected with code {close_code}")
            # Leave room group
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
        except Exception as e:
            logger.error(f"Error in WebSocket disconnect: {str(e)}", exc_info=True)

    # Receive message from WebSocket
    async def receive(self, text_data):
        try:
            logger.info(f"Received message: {text_data}")
            text_data_json = json.loads(text_data)
            message_type = text_data_json.get('type', 'message')
            
            if message_type == 'ping':
                # Echo back for ping
                await self.send(text_data=json.dumps({
                    'type': 'pong',
                    'message': 'Connection active'
                }))
                return
                
            message = text_data_json.get('message', '')
            
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'notification_message',
                    'message': message
                }
            )
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON received: {text_data}")
            await self.send(text_data=json.dumps({
                'error': 'Invalid JSON format'
            }))
        except Exception as e:
            logger.error(f"Error in WebSocket receive: {str(e)}", exc_info=True)
            await self.send(text_data=json.dumps({
                'error': 'Server error processing message'
            }))

    # Receive message from room group
    async def notification_message(self, event):
        try:
            message = event['message']
            
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': message
            }))
        except Exception as e:
            logger.error(f"Error in notification_message: {str(e)}", exc_info=True)