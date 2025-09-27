"""
100% static block initialization in python not possible. Because,
class LoggerSingleton:
   _instance = LoggerSingleton()

For Above Python will throw an error: NameError: name 'LoggerSingleton' is not defined

Python reads the class body top to bottom. At the moment we try _instance = LoggerSingleton(), the class
LoggerSingleton is not fully defined yet. So we cannot create an instance of the class while defining the
class itself — unlike Java.

So, 100% Static Block Initialization in Python not Possible.
"""

class LoggerSingleton:
    def __new__(cls, *args, **kwargs):
        raise Exception("Use get_instance() method.")

    try:
        print("Static Block: Initializing LoggerSingleton")

        class _Logger:
            def __init__(self):
                print("Logger Initialized")
                self.logs = []

            def log(self, message):
                self.logs.append(message)
                print(f"[Log]: {message}")

            def get_logs(self):
                return self.logs

        _instance = _Logger()
    except Exception as e:
        raise RuntimeError(f"Failed to initialize LoggerSingleton: {e}")

    @classmethod
    def get_instance(cls):
        return cls._instance


if __name__ == '__main__':
    logger_1 = LoggerSingleton.get_instance()
    logger_2 = LoggerSingleton.get_instance()

    print(logger_1 is logger_2)


"""
- In Python code, _instance is actually a different class _Logger, not LoggerSingleton.
- So technically, LoggerSingleton itself is never instantiated, only _Logger is.
- This works, but it’s not the same as Java — it’s a wrapper around a nested class.
"""
