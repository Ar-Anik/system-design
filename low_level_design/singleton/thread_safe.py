import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ThreadSafeSingleton._instance is not None:
            raise Exception("Use get_instance() instead of creating object directly.")
        print("Initializing ThreadSafeSingleton...")

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = ThreadSafeSingleton()
        return cls._instance


if __name__ == '__name__':
    s1 = ThreadSafeSingleton.get_instance()
    s2 = ThreadSafeSingleton.get_instance()

    print(s1 is s2)

"""
1. _lock = threading.Lock() → Ensures only one thread can enter get_instance() at a time.
2. with cls._lock: → guarantees safe creation of the singleton in multi-threaded scenarios.
3. Lazy initialization → the object is created only when first requested.
"""
