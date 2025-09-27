from enum import Enum

class Logger:
    def __init__(self):
        print("Logger Initialized")
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(f"[Log]: {message}")

    def get_logs(self):
        return self.logs


"""
Before Check In Python-OOP, __getattribute__vs__getattr__.py
"""

class LoggerSingleton(Enum):
    Instance = Logger()

    def __getattr__(self, item):
        """
        In Python, enum members (like LoggerSingleton.Instance) are objects of the enum class (LoggerSingleton).
        Every enum member has an internal attribute called _value_, which stores the actual value we assigned.
        """
        print("this is __getattr__")
        value = object.__getattribute__(self, "_value_")
        return getattr(value, item)

if __name__ == "__main__":
    logger_1 = LoggerSingleton.Instance
    logger_2 = LoggerSingleton.Instance

    print(logger_1 is logger_2)

    logger_1.log("First Message.")
    logger_2.log("Second Message")

    print(logger_1.get_logs())

"""
1. logger_1 = LoggerSingleton.Instance and logger_2 = LoggerSingleton.Instance
Both logger_1 and logger_2 point to the same enum member (LoggerSingleton.Instance). No __getattr__ is triggered 
here because .Instance is a defined attribute on the enum class.

2. print(logger_1 is logger_2)
- is checks object identity.
- Both are the same enum member → result is True.
- Before printing True, Python looks up __str__ / __format__ inside Enum machinery.
- Our LoggerSingleton doesn’t have these directly, so it falls back to __getattr__
- And Output:
    this is __getattr__
    True

3. logger_1.log("First Message.")
- logger_1 is an enum member, not a Logger.
- When we call .log, Python first looks in LoggerSingleton (the enum member).
- It doesn’t find log → triggers __getattr__.
- Our __getattr__ fetches _value_ (the real Logger object) and forwards .log.
- Then the Logger.log() method runs.
- And Output: 
    this is __getattr__
    [Log]: First Message.
"""

"""
It is 100% Enum Singleton in Python. It is Thread Safe : 
- Enum members are created when the class is first loaded.
- Python guarantees one-time initialization for enum members, even in multithreaded code.
- So we don’t need additional locks.
"""
