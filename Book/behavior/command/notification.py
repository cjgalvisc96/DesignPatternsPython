from abc import ABC, abstractmethod
from typing import Dict


class NotificationService(object):
    def send_email(self, *, data):
        print(f"Sending email = {data}")

    def send_sms(self, *, data):
        print(f"Sending SMS = {data}")


class NotificationInvoker(object):
    def __init__(self) -> None:
        self.notification_history = []

    def invoke(self, *, command):
        self.notification_history.append(command)
        command.execute()


class BaseCommand(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError("Please implement in subclass")


class EmailCommand(BaseCommand):
    def __init__(self, *, receiver: NotificationService, data: Dict) -> None:
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_email(data=self.data)


class SMSCommand(BaseCommand):
    def __init__(self, *, receiver: NotificationService, data: Dict) -> None:
        self.receiver = receiver
        self.data = data

    def execute(self):
        self.receiver.send_sms(data=self.data)


if __name__ == "__main__":
    invoker = NotificationInvoker()
    sender = NotificationService()
    invoker.invoke(command=EmailCommand(receiver=sender, data={"subject": "Test Email"}))
    invoker.invoke(command=SMSCommand(receiver=sender, data={"subject": "Test SMS"}))
    print(invoker.notification_history)
