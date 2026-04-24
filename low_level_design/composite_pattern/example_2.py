"""
Link-2 : https://refactoring.guru/design-patterns/composite
"""

"""
Composite হলো এমন একটি Structural Design Pattern যার মাধ্যমে object গুলোকে tree মতো কাঠামোতে সাজানো যায় এবং পরবর্তীতে এই পুরো কাঠামোটিকে 
একটি individual objects হিসেবে বিবেচনা করে কাজ করা যায়।
"""

"""
--------
Problem
--------
Composite Pattern ব্যবহার করা তখনই যৌক্তিক, যখন কোনো application এর core model-টিকে একটি tree হিসেবে উপস্থাপন করা সম্ভব হয়।

উদাহরণস্বরূপ, ধরা যাক দুই ধরনের Object রয়েছে: Products এবং Boxes। একটি Box-এর ভেতর বেশ কিছু প্রোডাক্টের পাশাপাশি ছোট আকারের আরও কিছু Box 
থাকতে পারে। এই ছোট Box গুলোর ভেতরেও আবার Products অথবা তার চেয়েও ছোট Box থাকতে পারে এবং এভাবেই চলতে থাকে।

ধরা যাক, এই Class গুলো ব্যবহার করে একটি Ordering System তৈরি করার সিদ্ধান্ত নেওয়া হলো। একটি Order-এর মধ্যে কোনো order box/packet/মোড়ক 
ছাড়া সাধারণ Product থাকতে পারে, আবার Product ও অন্যান্য Box দিয়ে ভর্তি box ও থাকতে পারে। এ ধরনের একটি Order-এর মোট Price কীভাবে নির্ধারণ 
করা সম্ভব?

সরাসরি একটি পদ্ধতি চেষ্টা করে দেখা যেতে পারে, সবগুলো Box খোলা, প্রতিটি Product Check করা এবং তারপর মোট দাম হিসাব করা। বাস্তব জগতে এটি করা সম্ভব 
হলেও, একটি প্রোগ্রামের ক্ষেত্রে এটি কেবল একটি loop চালানোর মতো সহজ কাজ নয়। এক্ষেত্রে যেসব Product ও Box নিয়ে কাজ করা হচ্ছে তাদের Class, Box গুলো 
কতগুলো স্তরে/level-এ সাজানো (nesting level) আছে এবং অন্যান্য Complex বিষয়গুলো আগে থেকেই জানা থাকতে হবে। এসব কারণে এই সরাসরি পদ্ধতিটি 
ব্যবহার করা অত্যন্ত অসুবিধাজনক অথবা ক্ষেত্রবিশেষে অসম্ভব হয়ে দাঁড়ায়।
"""

"""
--------
Solution
---------
Composite pattern এই সমস্যার সমাধানে Product ও Box গুলোর জন্য একটি common interface ব্যবহার করার প্রস্তাব দেয়, যেখানে মোট দাম হিসাব করার 
জন্য একটি method ঘোষণা করা থাকে।

এই মেথডটি কীভাবে কাজ করবে? একটি Product-এর ক্ষেত্রে, এটি সরাসরি ওই Product-এর দাম return করবে। একটি Box-এর ক্ষেত্রে, এটি Box-এর ভেতরে 
থাকা প্রতিটি Item-এর কাছে গিয়ে তাদের দাম জানতে চাইবে এবং তারপর ওই Box-এর মোট দাম return করবে। যদি এই item গুলোর মধ্যে কোনোটি একটি ছোট 
Box হয়, তবে সেই Box-টিও একইভাবে তার ভেতরের উপাদানগুলোর দাম হিসাব করতে শুরু করবে এবং ভেতরের সব উপাদানের দাম হিসাব না হওয়া পর্যন্ত এই প্রক্রিয়া 
চলতেই থাকবে। এমনকি একটি Box-এ caculated দামের সাথে কিছু অতিরিক্ত price ও যোগ করতে পারে, যেমন— packaging cost।

এই পদ্ধতির সবচেয়ে বড় সুবিধা হলো, Tree-কাঠামো গঠনকারী object গুলোর concrete classes নিয়ে মাথা ঘামানোর কোনো প্রয়োজন হয় না। একটি Object 
সাধারণ কোনো Product নাকি কোনো Complex Box, তা জানারও দরকার নেই। সাধারণ interface-টির মাধ্যমে এদের সবাইকে একইভাবে বিবেচনা করা যায়। যখন 
কোনো Composite Object-এ (Boxs) Method Call করা হয়, সে তার child object গুলোর ওপর সেই একই Method কল করে, এবং এভাবে Request-টি 
Tree-এর Leaf পর্যন্ত পৌঁছে যায়।
"""

"""
--------------------
Real-World Analogy
--------------------
বিশ্বের বেশিরভাগ দেশের সেনাবাহিনী hierarchy বা স্তরভিত্তিক কাঠামোতে সাজানো থাকে। একটি সেনাবাহিনী কয়েকটি division নিয়ে গঠিত হয়; একটি division 
হলো set of brigades, এবং একটি brigade গঠিত হয় platoons দিয়ে, যেগুলোকে আবার squads-এ ভাগ করা যায়। সবশেষে একটি squad হলো প্রকৃত 
সৈন্যদের একটি ছোট দল। এই কাঠামোর একদম শীর্ষ পর্যায় থেকে আদেশ দেওয়া হয় এবং তা প্রতিটি স্তরে নিচের দিকে স্থানান্তরিত হতে থাকে, যতক্ষণ না পর্যন্ত প্রতিটি 
সৈন্য তার করণীয় সম্পর্কে জানতে পারে।
"""


"""
-----------
Structure
-----------
1. Component Interface: এটি এমন সব Operation বা function describe করে, যা tree-এর simple এবং complex উভয় ধরনের element-এর জন্যই 
Common।

2. Leaf: এটি হলো tree-এর একটি basic element, যার কোনো sub-element থাকে না। সাধারণত Leaf component গুলোই বেশিরভাগ Main কাজ সম্পন্ন 
করে থাকে, কারণ কাজ delegate করার মতো এদের অধীনে আর কেউ থাকে না।

3. Container/Composite: যার অধীনে Sub-Element (Leaf বা অন্যান্য Container) থাকে। একটি Container তার child বা অধীনস্থ উপাদানগুলোর 
concrete class সম্পর্কে কিছু জানে না। এটি শুধুমাত্র Component Interface-এর মাধ্যমে তার সমস্ত Sub-Element এর সাথে কাজ করে। কোনো request 
পাওয়ার পর, একটি Container তার অধীনস্থ Sub-Element গুলোকে কাজ delegate করে দেয়, তাদের থেকে প্রাপ্ত ফলাফলগুলো process করে এবং সবশেষে 
ক্লায়েন্টের কাছে চূড়ান্ত ফলাফল পাঠায়। 

4. Client: Client Component Interface এর মাধ্যমে সমস্ত Element-এর সাথে যোগাযোগ করে। এর ফলে Client tree-এর Simple কিংবা Composite 
যেকোনো Element-এর সাথেই একইভাবে কাজ করতে পারে।
"""

"""
---------
Code
---------
CompoundGraphic class টি হলো একটি Container, যা অন্যান্য compound shape সহ যেকোনো সংখ্যক sub-shape ধারণ করতে পারে। একটি সাধারণ 
shape-এর যেসব Method থাকে, একটি Compound শেপেরও ঠিক একই Method থাকে। তবে নিজে থেকে কোনো কাজ করার বদলে, একটি Compound shape তার 
অধীনস্থ সকল চাইল্ডের কাছে recursively request-টি পাঠিয়ে দেয় এবং প্রাপ্ত ফলাফলগুলো একত্রিত করে।
client code সকল shape ক্লাসের জন্য থাকা একটিমাত্র common interface-এর মাধ্যমে সবগুলো শেপের সাথে কাজ করে। ফলে এটি কোনো simple shape নাকি 
compound shape নিয়ে কাজ করছে, তা ক্লায়েন্টের জানার প্রয়োজন হয় না। client অত্যন্ত complex object structure নিয়ে কাজ করতে পারে, অথচ সেই 
structure তৈরি করা concrete class গুলোর ওপর নির্ভরশীল হতে হয় না।
"""

from abc import ABC, abstractmethod
from typing import List, Set, Optional

# Component: Abstract Base Class
class Graphic(ABC):
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


# Leaf: Basic Element
class Dot(Graphic):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(f"Drawing Dot at ({self.x}, {self.y})")


# Another Leaf: Extending basic elements
class Circle(Dot):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius

    def draw(self) -> None:
        print(f"Drawing Circle at ({self.x}, {self.y}) with radius {self.radius}")


# Composite: Container Element
class CompoundGraphic(Graphic):
    def __init__(self):
        self._children: List[Graphic] = []

    def add(self, child: Graphic) -> None:
        if child not in self._children:
            self._children.append(child)

    def remove(self, child: Graphic) -> None:
        try:
            self._children.remove(child)
        except ValueError as e:
            print(f'Error : {e}')

    def move(self, x: int, y: int) -> None:
        for child in self._children:
            child.move(x, y)

    def draw(self) -> None:
        print('\n------ Processing Compound Graphic Structure ------')
        for child in self._children:
            child.draw()
        print('------ End of Structure ------\n')


# Client Code
class ImageEditor:
    def __init__(self):
        self.all_graphics = CompoundGraphic()

    def load_initial_data(self) -> None:
        self.all_graphics.add(Dot(1, 0))
        self.all_graphics.add(Circle(1, 5, 5))

        sub_group = CompoundGraphic()
        sub_group.add(Dot(-1, 0))
        self.all_graphics.add(sub_group)

    def group_selected(self, components: List[Graphic]) -> None:
        group = CompoundGraphic()
        for component in components:
            group.add(component)
            self.all_graphics.remove(component)

        self.all_graphics.add(group)
        print('Grouping Completed. Rendering Update:')
        self.all_graphics.draw()


# Entry Point
if __name__ == '__main__':
    editor = ImageEditor()
    editor.load_initial_data()

    d1 = Dot(1, 10)
    d2 = Dot(2, 15)
    c1 = Circle(5, 0, 5)
    c2 = Circle(3, 3, 5)

    editor.all_graphics.add(d1)
    editor.all_graphics.add(c1)

    editor.group_selected([d2, c2])


"""
---------------
Applicability
---------------
-> Tree Like Object Structure তৈরি করার ক্ষেত্রে, যখন কোনো Data বা Model কে একটি Tree-এর মতো সাজানোর প্রয়োজন হয়, তখন Composite 
Pattern ব্যবহার করা উচিত। এটি একটি common interface-এর অধীনে দুই ধরনের element প্রদান করে: 
    1. simple leaves 
    2. complex containers
একটি container leaf এবং অন্যান্য container উভয়টি নিয়েই গঠিত হতে পারে। এর ফলে এমন একটি nested recursive object structure তৈরি 
করা সম্ভব হয়, যা দেখতে একটি Tree-এর মতো।

-> Simple এবং Complex Element কে একইভাবে পরিচালনা করার ক্ষেত্রে, যখন Client কোডের মাধ্যমে Simple এবং Composite—উভয় ধরনের Element কে 
কোনো পার্থক্য না করে একইভাবে পরিচালনা করার প্রয়োজন পড়ে, তখন এই pattern টি কার্যকর। Composite Pattern-এ সংজ্ঞায়িত সকল Element একটি 
সাধারণ Interface share করে। এই interface টি ব্যবহার করার ফলে, client যেসব object নিয়ে কাজ করছে, সেগুলোর concrete class নিয়ে 
Client কে আর ভাবতে হয় না।
"""


"""
-----------------
How to Implement
-----------------
1. প্রথমেই নিশ্চিত করতে হবে যে, Application-এর Main Model-কে একটি Tree Structure হিসেবে উপস্থাপন করা সম্ভব। এটিকে ভেঙে simple elements 
এবং containers-এ ভাগ করতে হবে। খেয়াল রাখা জরুরি যে, Container গুলো যেন simple element এবং অন্যান্য Container—উভয়টিকেই ধারণ করতে 
সক্ষম হয়।

২. Simple এবং Composite উভয় ধরনের Component-এর জন্য যৌক্তিক ও similar মেথডের একটি তালিকা তৈরি করে Component Interface টি declare 
করতে হবে।

৩. Simple Element গুলোকে represent করার জন্য একটি leaf class তৈরি করতে হবে। একটি প্রোগ্রামে একাধিক ভিন্ন ভিন্ন leaf class থাকতে পারে।

৪. Composite Element গুলোকে represent করার জন্য একটি Container class তৈরি করতে হবে। এই ক্লাসে Sub-Element গুলোর reference সংরক্ষণ 
করার জন্য একটি array or list field রাখতে হবে। যেহেতু array-তে leaf এবং container—উভয়টিই সংরক্ষণ করতে হবে, তাই এটিকে অবশ্যই Component 
interface টাইপের মাধ্যমে declare করতে হবে।

৫. Component Interface-এর Method গুলো Implement করার সময় মনে রাখা প্রয়োজন যে, একটি Container মূলত তার Sub-Element গুলোর কাছে 
বেশিরভাগ কাজ delegate করে থাকে।

৬. সবশেষে, কন্টেইনারের মধ্যে child elements Add এবং Remove করার Method গুলো define করতে হবে।

Special Note: উপরের সব Method গুলো সরাসরি component interface-এ declare করা যেতে পারে। তবে এটি Interface Segregation Principle 
কে break করে, কারণ leaf ক্লাসের ক্ষেত্রে Method গুলো empty থেকে যাবে। তা সত্ত্বেও, এর মাধ্যমে client tree তৈরি করার সময়ও সব Elmenet কে সমানভাবে 
বিবেচনা করতে সক্ষম হয়।
"""


"""
----------------
Pros and Cons
----------------
-> Pros
1. Complex Tree Structure নিয়ে অত্যন্ত সুবিধাজনক উপায়ে কাজ করা যায়। polymorphism এবং recursion ব্যবহারের পূর্ণ সুবিধা পাওয়া যায়।

2. Open/Closed Principle অনুসরণ করে। Object Tree নিয়ে কাজ করছে—এমন Existing Code Break না করে Application-এ new Element 
অনায়াসে Add করা সম্ভব হয়।

-> Cons
1. যেসব ক্লাসের কার্যকারিতা বা ফাংশনালিটির মধ্যে খুব বেশি পার্থক্য রয়েছে, তাদের জন্য একটি Common Interface প্রদান করা বেশ কঠিন হতে পারে। কিছু নির্দিষ্ট 
ক্ষেত্রে, Component Interface-টিকে overgeneralize করার প্রয়োজন পড়তে পারে, যা পরবর্তীতে কোডটিকে বোঝা কঠিন করে তোলে।
"""
