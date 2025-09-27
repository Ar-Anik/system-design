"""
Q : What is Singleton Eager Initialization?
- Singleton Pattern: Ensures only one instance of a class exists throughout the program.
- Eager Initialization: The instance is created immediately at class loading time (not when it’s first requested).

This guarantees thread-safety because the instance is created before any thread accesses it, but the downside is:
    - If the instance is never used, it still consumes memory/resources.
"""

class EagerSingleton:
    _instance = None

    def __init__(self):
        if EagerSingleton._instance:
            raise Exception("This class is a singleton! use get_instance()")

    @classmethod
    def get_instance(cls):
        return cls._instance

# Instance is created eagerly (at class load time)
EagerSingleton._instance = EagerSingleton()

if __name__ == '__main__':
    s1 = EagerSingleton.get_instance()
    s2 = EagerSingleton.get_instance()

    print(s1 is s2)

    # s3 = EagerSingleton()

"""
* EagerSingleton._instance = EagerSingleton() is executed right after the class definition, so the instance is created eagerly.
* __init__ raises an exception if someone tries EagerSingleton(), enforcing the singleton rule.
* Access to the instance is only via get_instance().
"""

"""
# Use Cases of Eager Initialization Singleton
    1. Logger System
    2. Configuration Manager
    3. Global Cache Manager
    4. Database Connection Poolf
"""
