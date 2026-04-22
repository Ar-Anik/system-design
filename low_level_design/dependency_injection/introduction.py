"""
Link-1 : https://www.geeksforgeeks.org/system-design/dependency-injectiondi-design-pattern/
Link-2 : https://www.geeksforgeeks.org/python/what-is-a-pythonic-way-for-dependency-injection/
Link-3 : https://www.youtube.com/watch?v=0Lb20uEdd6Y&list=PLEnX8KcBFtGX6PgAjJypSKWMuQNWaTvnD&index=3

Imagine we're building an application that sends notifications to users. We want to make the notification system
flexible so we can change the notification provider (email, SMS, push notifications, etc.) without modifying the core
application logic.
"""

# WithOut Dependency Injection
class EmailProvider:
    @staticmethod
    def send_email(message, recipient):
        print(f"Sending Email to {recipient} : {message}")


class NotificationService:
    def __init__(self):
        self.email_provider = EmailProvider()

    def send_notification(self, message, recipient):
        self.email_provider.send_email(message, recipient)


service = NotificationService()
service.send_notification("Hello World", "anik@gmail.com")


# With Dependency Injection

# 1. Interface
from abc import ABC, abstractmethod

class NotificationProvider(ABC):
    @abstractmethod
    def send_notification(self, message, recipient):
        pass


# 2. Service
class EmailProvider(NotificationProvider):
    def send_notification(self, message, recipient):
        print(f"Email To: {recipient} | Message: {message}")


class SMSProvider(NotificationProvider):
    def send_notification(self, message, recipient):
        print(f"SMS To: {recipient} | Message: {message}")


# Client
class NotificationService:
    def __init__(self, notification_provider: NotificationProvider):
        self.notification_provider = notification_provider

    def send_notification(self, message, recipient):
        self.notification_provider.send_notification(message, recipient)


# Injector
email_service = NotificationService(EmailProvider())
email_service.send_notification('Hello via Email', 'aranik@gmail.com')

sms_service = NotificationService(SMSProvider())
sms_service.send_notification('Hello via SMS', '+01685946475')


# Dependency Injection
class Engine:
    def start(self):
        print("Engine Started")


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is Driving")


if __name__ == '__main__':
    engine = Engine()
    car = Car(engine)

    car.drive()


# Setter Injection
class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine

    def drive(self):
        if self.engine is None:
            raise RuntimeError("Engine is not set! Please inject Engine before driving.")

        self.engine.start()
        print("Car is Driving.")


if __name__ == '__main__':
    engine = Engine()

    car = Car()
    car.set_engine(engine)

    car.drive()


# Interface Injection
from abc import ABC, abstractmethod

class Engine:
    def start(self):
        print("Engine Started")


class DependencyInjector(ABC):
    @abstractmethod
    def inject_dependency(self, engine: Engine):
        pass

class Car(DependencyInjector):
    def __init__(self):
        self.engine = None

    def inject_dependency(self, engine: Engine):
        self.engine = engine

    def drive(self):
        if self.engine is None:
            raise RuntimeError("Engine is not injected! Please inject Engine before driving.")

        self.engine.start()
        print("Car is Driving")

if __name__ == '__main__':
    engine = Engine()

    car = Car()
    car.inject_dependency(engine)

    car.drive()

