from typing import List
import datetime
from abc import ABC,abstractmethod


class User:
    def __init__(self, name: str, contact_info: str, conversations: List['Conversation'] = None) -> None:
        self.name = name
        self.contact_info = contact_info
        self.conversations = conversations if conversations is not None else []

    def create_conversation(self, user: 'User') -> 'Conversation':
        conversation = Conversation(participants=[self, user])
        self.conversations.append(conversation)
        user.conversations.append(conversation)
        return conversation

    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        if conversation in self.conversations:
            conversation.add_message(message)
        else:
            raise ValueError("Conversation not found")

    def receive_message(self, message: 'Message') -> None:
        if message.conversation in self.conversations:
            print(f"Message from {message.sender.name}")
            message.display_content()
        else:
            raise ValueError("Message not from conversation")

    def manage_settings(self) -> None:
        print(f"Managing settings for {self.name}")

    def get_conversations(self) -> List['Conversation']:
        return self.conversations
    
class Conversation:
    def __init__(self, participants: List['User']) -> None:
        self.participants = participants
        self.message_history = []

    def add_message(self, message: 'Message') -> None:
        self.message_history.append(message)

    def add_user(self, user: 'User') -> None:
        if user not in self.participants:
            self.participants.append(user)
        else:
            print("User is already in the conversation")

    def get_messages(self) -> List['Message']:
        return self.message_history

class Message:
    def __init__(self, sender: 'User', conversation: 'Conversation', timestamp: datetime.datetime) -> None:
        self.sender = sender
        self.conversation = conversation
        self.timestamp = timestamp

    def display_content(self) -> None:
        raise NotImplementedError("Subclasses should implement this!")

    def get_message_type(self) -> str:
        raise NotImplementedError("Subclasses should implement this!")

class TextMessage(Message):
    def __init__(self, content: str, sender: 'User', conversation: 'Conversation', timestamp: datetime.datetime) -> None:
        super().__init__(sender, conversation, timestamp)
        self.content = content

    def display_content(self) -> None:
        print(f"TextMessage from {self.sender.name}: {self.content}")

    def get_message_type(self) -> str:
        return "Text"
    
class MultimediaMessage(Message):
    def __init__(self, file_path: str, media_type: str, sender: User, conversation: Conversation, timestamp: datetime.datetime) -> None:
        super().__init__(sender,conversation,timestamp)
        self.file_path = file_path 
        self.media_type = media_type
    def display_content(self) -> None:
        print(f"file path: {self.file_path} Message type: {self.media_type}")
    def get_message_type(self) -> str:
        return self.media_type
    
class MessagingManager(ABC):

    @abstractmethod
    def send_message(self, message: Message) -> None:
        pass

    @abstractmethod
    def receive_message(self, message: Message) -> None:
        pass

    @abstractmethod
    def view_conversation_history(self, conversation: Conversation) -> List[Message]:
        pass

class SimpleMessagingManager(MessagingManager):
    def __init__(self):
        self.conversations: List[Conversation] = []

    def send_message(self, message: Message) -> None:
        message.conversation.add_message(message)
        print(f"Message sent by {message.sender.name}")

    def receive_message(self, message: Message) -> None:
        print(f"Message received by {message.conversation.participants[0].name}")
        message.display_content()

    def view_conversation_history(self, conversation: Conversation) -> List[Message]:
        return conversation.get_messages()

def main():

    try:
        user1 = User(name="James", contact_info="@example.com")
        user2 = User(name="Ann", contact_info="@example.com")

        conversation = user1.create_conversation(user2)

        messaging_manager = SimpleMessagingManager()

        text_message1 = TextMessage(content="Hello, Bob!", sender=user1, conversation=conversation, timestamp=datetime.datetime.now())
        user1.send_message(text_message1, conversation)
        messaging_manager.send_message(text_message1)

        text_message2 = TextMessage(content="Hi Alice, how are you?", sender=user2, conversation=conversation, timestamp=datetime.datetime.now())
        user2.send_message(text_message2, conversation)
        messaging_manager.send_message(text_message2)

        history = messaging_manager.view_conversation_history(conversation)
        print("\nConversation History:")

        for message in history:
            message.display_content()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()