class LazySingleton:
    _instance = None
    _initialization = True

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Create Lazysingleton Object...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if self._initialization:
            print("Initializing Start")
            self.name = name
            # self.__class__._initialization = False
            self._initialization = False

    def __str__(self):
        return self.name

if __name__ == '__main__':
    s1 = LazySingleton("s1")
    s2 = LazySingleton("s2")

    print(s1 is s2)

    print(s1.name)
    print(s2.name)
