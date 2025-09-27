"""
One Single Entry Point.
"""

class LazySingleton:
    _instance = None
    _allow_init = False

    def __init__(self):
        if not LazySingleton._allow_init:
            raise Exception("Use get_instance() to access the singleton.")
        print("Initializing LazySingleton...")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._allow_init = True
            cls._instance = LazySingleton()
            cls._allow_init = False
        return cls._instance

if __name__ == "__main__":
    s1 = LazySingleton.get_instance()
    s2 = LazySingleton.get_instance()

    print("s1 is s2:", s1 is s2)  # True → same object

    s3 = LazySingleton()
