"""
Bangla-Link : https://software-engineering-notes-in-bangla.blogspot.com/2019/09/observer-design-pattern.html (Code Below)

Link : https://www.geeksforgeeks.org/system-design/observer-pattern-set-1-introduction/

-> The Observer Design Pattern is a behavioral design pattern that defines a one-to-many dependency between objects. When
one object (the subject) changes state, all its dependents (observers) are notified and updated automatically.

-> In the Observer pattern, we typically need four main components to build it properly.
1. Subject (Publisher) Interface
Role: Declares methods for adding, removing, and notifying observers.
Why: This ensures all concrete subjects follow the same communication rules.

2. Concrete Subject (Concrete Publisher)
Role: Maintains the state, keeps track of observers, and sends updates when something changes.
Why: This is the actual object that observers are interested in.

3. Observer Interface
Role: Declares the update() method that all observers must implement.
Why: Ensures all observers can receive updates in a consistent way.

4. Concrete Observer
Role: Implements the update() method and reacts to changes from the subject.
Why: These are the actual subscribers who take action on updates.

5. Optional Extra (in some designs):
Event Manager / Helper Class – If we want to separate subscription logic from the subject, we can have a separate event
manager (composition-based approach). (Example-1)
"""

from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def unregister(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, notification_msg):
        pass


class FacebookPage(Subject):
    def __init__(self, name):
        self.name = name
        self._observers: List[Observer] = []
        self._status = None

    def register(self, observer):
        if isinstance(observer, Observer):
            self._observers.append(observer)

    def unregister(self, observer):
        if isinstance(Observer, observer):
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(f'From {self.name} Page. {self._status}')

    def update_page(self, status):
        self._status = status
        self.notify_observers()

class FacebookAccount(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, notification_msg):
        print(f'{self.name} Has New Notification. {notification_msg}')

class ObserverPatternTestDrive:
    def main(self):
        fb_page = FacebookPage("Ar-Anik")

        account_1 = FacebookAccount("Sourov")
        account_2 = FacebookAccount("Sisir")

        fb_page.register(account_1)
        fb_page.register(account_2)

        fb_page.update_page("This Page Now Live")

if __name__ == '__main__':
    ObserverPatternTestDrive().main()
