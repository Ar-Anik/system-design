"""
> High level modules should not depend on low-level modules, both should depend on abstractions.

> Abstract should not depend on details. Details should depend on abstractions.
Here, Abstract = Interface or Abstract class (the "contract")
Details = Concrete implementations (the "how things are done")
-> A concrete implementation is a derived class (child class) that implements all the abstract methods
of its abstract base class (parent class).

# Abstract class (defines WHAT to do)
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):  # Concrete implementation
    def speak(self):
        return "Woof!"
"""

# Example that violated DIP
class GoogleAuthenticationService:
    def authenticate(self, email):
        return True

class UserLogin:
    def login(self, email):
        # DIP is violated here because we're directly depending on a concrete class
        google_authentication = GoogleAuthenticationService()
        auth_result = google_authentication.authenticate(email)

        if auth_result:
            return True

login = UserLogin()
print(login.login('aubdurrobanik@gmail.com'))


"""
To follow the Dependency Inversion Principle, you should depend on an abstraction rather than a concrete class.
"""

from abc import ABC, abstractmethod

class AuthenticationService(ABC):
    @abstractmethod
    def authenticate(self, email):
        pass

class GoogleAuthenticationService(AuthenticationService):
    def authenticate(self, email):
        return True

class GithubAuthenticationService(AuthenticationService):
    def authenticate(self, email):
        return True

class UserLogin:
    def login(self, email, authentication_service:AuthenticationService):
        # Dependency Inversion Principle: depend on abstraction
        auth_result = authentication_service.authenticate(email)
        if auth_result:
            return True

login = UserLogin()
login.login('aubdurrobanik@gmail.com', GithubAuthenticationService())

"""
> AuthenticationService: Acts as an interface via Python’s ABC module.
> GoogleAuthenticationService and GithubAuthenticationService: Concrete implementations.
> UserLogin doesn’t care what kind of auth service is passed; it just calls authenticate() on the abstraction.
> We can now easily switch strategies without changing the UserLogin class.

Here, High Level Code(UserLogin) and Low Level Code(GoogleAuthenticationService, GithubAuthenticationService) depend on abstract method.
"""

"""
Benefits:
    * Loose coupling: Reduces direct dependencies between components.
    * Better testability: Easier to use mocks/stubs for unit testing.
    * Greater flexibility and reuse: Modules can be swapped out with minimal changes.
    * Clear separation of concerns: Enhances system structure and maintainability.
"""
