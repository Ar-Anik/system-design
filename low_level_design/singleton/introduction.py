"""
Link : https://refactoring.guru/design-patterns/singleton?utm_source=chatgpt.com
Link : https://blog.algomaster.io/p/singleton-design-pattern
Link : https://medium.com/গণকযন্ত্র/সিঙ্গেলটন-প্যাটার্ন-1526a0def3db/
Link : https://algomaster.io/learn/lld/dependency
"""

"""
- সিঙ্গেলটন প্যাটার্ন(Singleton Pattern) হল ক্রিয়েশনাল ডিজাইন প্যাটার্ন যার একটি ক্লাসে(class) শুধুমাত্র একটি instance থাকবে এবং একটা global 
access point থাকবে ওই instance টা ব্যবহার করার জন্য।

- সিঙ্গেলটন প্যাটার্ন ২ টা সমস্যা সমাধান করে কিন্তু একই সাথে এটি Single Responsibility Principle break করে।
"""

"""
_lock = threading.Lock()

Q: What is a Lock?
- A Lock (from Python’s threading module) is a synchronization primitive. It allows only one thread at a time 
to acquire the lock. Other threads trying to acquire the lock must wait until it’s released.
- Think of it like a toilet key in an office:  Only one person can enter at a time. If someone already has the 
key (lock acquired), others must wait until they release it.

Q: Why do we need it in a Singleton?
- The singleton must ensure that only one instance of the class is created, even if multiple threads run at the 
same time. 

# Without a lock:
- Thread A checks _instance → it’s None.
- Thread B also checks _instance → still None (because A hasn’t finished yet).
- Both threads create a new Database() instance → two instances (breaks Singleton).

# With a lock:
- Thread A acquires the lock → goes inside → creates the instance.
- Thread B waits until the lock is released.
- By the time Thread B checks again, _instance is already set → it reuses the same one.
"""

import threading

class Database:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if Database._instance is not None:
            raise Exception("Use get_instance() to access the Database Singleton.")

        print("Initializing Database Connection .... ")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = Database()
        print(f"Thread Name : {threading.current_thread().name}")
        return cls._instance

    def query(self, sql:str):
        print(f"Executing SQL : {sql}")


if __name__ == '__main__':
    instance_1 = Database.get_instance()
    instance_1.query("SELECT * FROM users")

    instance_2 = Database.get_instance()
    instance_2.query("SELECT * FROM products")

    instance_3 = Database()

    print(instance_1 is instance_2)

"""
Use Case of Lazy initialization singleton : 

1. Third-Party API Client (Pay-per-Use APIs)
Example: Payment gateway or external API where each session costs money or resources.
Initialize the API client, only when the first request to that service happens. After that, the same instance is reused.
It Avoid unnecessary connection/cost and Centralized session management.
"""