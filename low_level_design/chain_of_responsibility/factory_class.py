"""
-> A factory class is a class whose main job is to create and configure objects — kind of like a “construction workshop” for our program.

> In the context of Chain of Responsibility:
    * We might have several handler objects (like Level1SupportHandler, Level2SupportHandler, ManagerSupportHandler).
    * These handlers need to be linked in a certain order to form a chain.
    * The factory class would be responsible for building this chain automatically, based on some configuration or
      environment setting — instead of making the client manually link them one by one.

> Why use a factory class here?
    * Centralized creation logic – All the steps to assemble the chain are in one place.
    * Configurable behavior – The factory can build different chains based on environment variables, JSON config, or user role.
    * Reduces client complexity – The client just says “Give me a chain”, not “Let me wire the handlers manually”.
"""

from abc import ABC, abstractmethod
from enum import Enum

class Difficulty(Enum):
    Easy = 1
    Medium = 2
    Hard = 3
    Unknown = 99

class SupportRequest:
    def __init__(self, issue: str, level: Difficulty):
        self.issue = issue
        self.level = level

class SupportHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, request: SupportRequest):
        pass


class LevelOneSupportHandler(SupportHandler):
    def handle_request(self, request: SupportRequest):
        if request.level == Difficulty.Easy:
            print(f"Level 1 Support: Handling '{request.issue}'")
        elif self.next_handler:
            self.next_handler.handle_request(request)
        else:
            print("No one available to handle this request.")


class LevelTwoSupportHandler(SupportHandler):
    def handle_request(self, request: SupportRequest):
        if request.level == Difficulty.Medium:
            print(f"Level 2 Support: Handling '{request.issue}'")
        elif self.next_handler:
            self.next_handler.handle_request(request)
        else:
            print("No one available to handle this request.")


class ManagerSupportHandler(SupportHandler):
    def handle_request(self, request: SupportRequest):
        if request.level == Difficulty.Hard:
            print(f"Manager: Handling '{request.issue}'")
        elif self.next_handler:
            self.next_handler.handle_request(request)
        else:
            print("No one available to handle this request.")


class SupportChainFactory:
    def __init__(self, config: dict):
        """
        config example:
        {
            "include_manager": True,
            "include_level2": True
        }
        """
        self.config = config

    def create_chain(self):
        # Always start with level 1
        level_1 = LevelOneSupportHandler()
        current = level_1

        if self.config.get("include_level_2"):
            current = current.set_next(LevelTwoSupportHandler())

        if self.config.get("include_manager"):
            current = current.set_next(ManagerSupportHandler())

        return level_1


if __name__ == '__main__':
    # Config could come from JSON, DB, env vars, etc.
    config = {
        "include_manager": True,
        "include_level_2": True
    }

    request = [
        SupportRequest("Password reset", Difficulty.Easy),
        SupportRequest("Database connection issue", Difficulty.Medium),
        SupportRequest("System outage", Difficulty.Hard),
        SupportRequest("Unknown issue", Difficulty.Unknown)
    ]

    factory = SupportChainFactory(config)
    support_chain = factory.create_chain()

    for req in request:
        support_chain.handle_request(req)

