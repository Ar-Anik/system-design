"""
Lazy initialization means:
    - The singleton instance is not created immediately when the class is loaded.
    - Instead, it is created only when it’s first requested (on demand).
So the object lives only if the program actually needs it.
"""

class LazySingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Object is created.")
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = LazySingleton()
        return cls._instance

if __name__ == '__main__':
    s1 = LazySingleton()
    s2 = LazySingleton()
    s3 = LazySingleton.get_instance()
    s4 = LazySingleton.get_instance()

    print(s1 is s2)
    print(s3 is s4)
    print(s1 is s2 is s3 is s4)

"""
- Above code not the cleanest 100% right lazy singleton because it mixes two mechanisms.
    1. __new__ based singleton
    2. get_instance()-based singleton

- The core idea of the singleton pattern is:
    1. One instance
    2. One way to access it globally

- If mix multiple access points (__new__ + get_instance()), it still technically have one instance, but it lose clarity 
and consistency, which makes the design weaker.
"""
