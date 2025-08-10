from abc import ABC, abstractmethod
from collections import defaultdict

class EventManager:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, listener):
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        if listener in self.listeners[event_type]:
            self.listeners[event_type].remove(listener)

    def notify(self, event_type, data):
        for listener in self.listeners[event_type]:
            listener.update(data)


class NewsAgency:
    def __init__(self):
        self.events = EventManager()

    def publish_news(self, news):
        print(f"[NewsAgency] Publishing {news}")
        self.events.notify("news", news)

class EventListener(ABC):
    @abstractmethod
    def update(self, data):
        pass

class EmailSubscriber(EventListener):
    def __init__(self, email):
        self.email = email

    def update(self, data):
        print(f"[Email to {self.email}] News Update: {data}")

class SMSSubscriber(EventListener):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def update(self, data):
        print(f"[SMS to {self.phone_number}] News Update: {data}")

class Application:
    def config(self):
        news_agency = NewsAgency()

        email_subscriber = EmailSubscriber("anik@gmail.com")
        sms_subscriber = SMSSubscriber("01685946475")

        news_agency.events.subscribe("news", email_subscriber)
        news_agency.events.subscribe("news", sms_subscriber)

        return news_agency

if __name__ == '__main__':
    app = Application().config()

    app.publish_news("Python 3.14 Released.")
    app.publish_news("Anik Birthday is comming.")
