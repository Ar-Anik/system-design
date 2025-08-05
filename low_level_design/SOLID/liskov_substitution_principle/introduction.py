"""
Subtype/Derived = Child class
Superclass = Parent class
Substitutable = Replace

1. Objects in a program should be replaceable with instances of their subtypes without altering the correctness of
that program.

> Description :
"Objects in a program should be replaceable with instances of their subtypes”
⟶ This means: We should be able to use a child class object wherever a parent class object is expected.

"Without altering the correctness of that program"
-> This means: When we replace the parent object with a child object, the program should still behave
correctly — it shouldn’t crash, behave unexpectedly, or give wrong results.

2. Subclass/derived class should be substitutable for their base class.

> Description :
-> This means: If we write code that uses a base class, we should be able to use a subclass in its place,
and the code should still work correctly — without errors or unexpected behavior.

3. Objects of a superclass should be replaceable with objects of its subclasses without affecting the
correctness of the program.
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

def make_it_speak(animal: Animal):
    animal.speak()

make_it_speak(Dog())
make_it_speak(Cat())

"""
Benefits:
    * Reliable polymorphism: Derived classes can be used safely without breaking the system.
    * Robust inheritance: Encourages correct use of inheritance and abstraction.
    * Fewer bugs in OOP hierarchy: Prevents unexpected behaviors from subclasses.
    * Code predictability: Improves consistency in class behavior.
"""
