"""
1. A client should not be forced to implement an interface that it doesn’t use.
> In this context, a client is any class (or code) that uses or depends on an interface or class.
So, A class (client) shouldn't be forced to implement methods from an interface that it doesn't need or use.
"""

from abc import ABC, abstractmethod

class PrintrInterface(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def photocopy(self):
        pass

    @abstractmethod
    def scan(self):
        pass

class DigitalPrinter(PrintrInterface):
    def print(self):
        return 'Print'

    def photocopy(self):
        return 'Photocopy'

    def scan(self):
        return 'Scan'

# ModernPrinter violates ISP: it doesn't really support scan
class ModernPrinter(PrintrInterface):
    def print(self):
        return 'Print'

    def photocopy(self):
        return 'Photocopy'

    def scan(self):
        return 'Not Supported'    # ISP violation

# OldPrinter violates ISP: only supports printing
class OldPrinter(PrintrInterface):
    def print(self):
        return 'Print'

    def photocopy(self):
        return 'Not Supported'   # ISP violation

    def scan(self):
        return 'Not Supported'   # ISP violation


"""
The Interface Segregation Principle (ISP) focuses on splitting large interfaces into smaller, more specific ones, 
so that clients (classes or modules that use these interfaces) can choose only what they actually need — instead 
of being forced to implement methods they don’t use.
"""

from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Photocopiable(ABC):
    @abstractmethod
    def photocopy(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class DigitalPrinter(Printable, Photocopiable, Scannable):
    def print(self):
        return 'Print'

    def photocopy(self):
        return 'Photocopy'

    def scan(self):
        return 'Scan'

class ModernPrinter(Printable, Photocopiable):
    def print(self):
        return 'Print'

    def photocopy(self):
        return 'Photocopy'

class OldPrinter(Printable):
    def print(self):
        return 'Print'

"""
> It avoids unnecessary code (like return "Not supported").
> It makes code easier to maintain, extend, and test.
> It keeps the responsibility of each interface focused.
> It promotes flexibility — developers can mix only the parts they want.
"""

"""
Benefits:
    * Focused interfaces: Prevents bloated interfaces and unnecessary methods.
    * Improved flexibility: Clients can implement only what they need.
    * Better modularity: Interfaces are tailored to specific needs.
    * Easier refactoring and testing: Smaller interfaces are simpler to test and maintain.    
"""
