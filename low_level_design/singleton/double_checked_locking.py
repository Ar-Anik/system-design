import threading

class DoubleCheckedSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if DoubleCheckedSingleton._instance:
            raise Exception("Use get_instance() to access the singleton.")
        print("Initializing Double Check Singleton")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = DoubleCheckedSingleton()
        return cls._instance

if __name__ == '__main__':
    s1 = DoubleCheckedSingleton.get_instance()
    s2 = DoubleCheckedSingleton.get_instance()

    print(s1 is s2)


"""
1. First check (outside lock) → avoids unnecessary locking after instance is created.
2. Lock (with cls._lock) → ensures only one thread initializes the object.
"""
