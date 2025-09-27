"""
Python doesn’t have “static inner classes” in the same way as Java, but we can simulate the same logic using a nested class.
"""
import threading

class BillPughSingleton:
    class _Holder:
        instance = None
        lock = threading.Lock()

    def __new__(cls):
        raise RuntimeError("Use get_instance() instead.")

    @classmethod
    def get_instance(cls):
        if cls._Holder.instance is None:
            with cls._Holder.lock:
                if cls._Holder.instance is None:
                    cls._Holder.instance = super().__new__(cls)
        return cls._Holder.instance

s1 = BillPughSingleton.get_instance()
s2 = BillPughSingleton.get_instance()

print(s1 is s2)

"""
-> In Java, the Bill Pugh Singleton relies on class-loading guarantees of the JVM:
- The static inner class is loaded only once, automatically.
- This ensures thread-safe lazy initialization without any locks.

In Python, When multiple threads call get_instance() at the same time, Python does not automatically prevent two 
threads from creating the instance. That’s why, in Python, we must use locks to guarantee thread safety.

Using locks (double-checked or similar) solves the problem, but it breaks the “no synchronization needed” elegance of 
the original Bill Pugh pattern. So in Python:
We can implement a lazy singleton, But we cannot perfectly mimic the Java Bill Pugh Singleton without some form of 
synchronization.
"""