"""
Link-1(Bangla) : https://software-engineering-notes-in-bangla.blogspot.com/2019/05/composite-design-pattern.html

Link-2 : https://refactoring.guru/design-patterns/composite
"""

"""
Composite Design Pattern হলো একটি Structural Design Pattern, যা object গুলোকে একটি tree structure-এ organize করতে সাহায্য 
করে এবং individual object (leaf) ও object group (composite)-কে একইভাবে treat করার সুবিধা দেয়।

মনে করা যাক, একটি বড় উপহারের Box আছে। এই বাক্সের ভেতরে দুই ধরণের item থাকতে পারে:
১. সরাসরি কোনো উপহার (যেমন: একটি ঘড়ি বা একটি কলম)।
২. আরও ছোট ছোট কিছু বাক্স, যেগুলোর ভেতরে আবার উপহার আছে।

এখন যদি বলা হয়— "Box টি খোলো", তবে বড় Box-টি খোলা হবে, তার ভেতরের ছোট Box গুলোও খোলা হবে এবং সবশেষে মূল উপহারগুলো বের করা হবে।
এখানে ঘড়ি, কলম বা ছোট Box—সবগুলোকেই বাইরের থেকে একটি সাধারণ 'উপহার' হিসেবে দেখা হচ্ছে।

প্রতিটি উপহার (হোক তা ঘড়ি বা box) একই interface অনুসরণ করে, যেমন open() method। যখন open() call করা হয়, তখন leaf নিজেকে খুলে 
ফেলে, আর box তার ভিতরের সব item-এ একই open() call করে। এইভাবে single object এবং object group-কে একইভাবে treat করার 
প্যাটার্নই হলো Composite Design Pattern।

-> Composite Design Pattern-এর প্রধান উপাদানসমূহ
1. Component (Common Interface)
এটি হলো একটি সাধারণ Interface বা Abstract Class, যা Leaf এবং Composite—উভয় অবজেক্টের জন্যই সাধারণ Method গুলো (যেমন: open()) 
define করে দেয়।

2. Leaf (Individual Object)
Leaf হলো সেই Object যার কোনো Child নেই। এটি Tree Structure-এর একদম শেষ ধাপ। উপরের Example-এ :
ঘড়ি (Watch) বা কলম (Pen) হলো Leaf। যখন এদের উপর open() call করা হয়, তারা সরাসরি উপহারটি প্রদর্শন করে। এদের ভেতরে আর কোনো Box 
বা item থাকে না।

3. Composite (Object Group)
Composite হলো এমন একটি Object যার ভেতরে Leaf অথবা অন্য আরও কিছু Composite Object থাকতে পারে। এটি Component Interface 
Implement করে ঠিকই, কিন্তু এর কাজ হলো তার ভেতরে থাকা সব child item-এর কাজগুলোকে পরিচালনা করা।
উপরের Example-এ : বড় উপহারের Box বা ছোট Box গুলো হলো Composite। যখন বড় বক্সের উপর open() Call করা হয়, সে নিজে খোলার পাশাপাশি 
তার ভেতরের সব আইটেমের (Leaf/Composite) open() Method কে Recursively Call করে।

4. Client (User)
Client সরাসরি Component Interface ব্যবহার করে object গুলোর সাথে কাজ করে। সে জানেও না যে সে কি একটি Individual Object সাথে কাজ 
করছে নাকি Object Group সাথে কাজ করছে।
"""

from abc import ABC, abstractmethod

class Gift(ABC):
    @abstractmethod
    def open(self):
        pass

class Item(Gift):
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f"Opening {self.name}")

class Box(Gift):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def open(self):
        print(f'Opening {self.name}')
        for item in self.items:
            item.open()

# Leaf Items
watch = Item("Watch")
pen = Item("Pen")
book = Item("Book")
ring = Item("Ring")

# Small Box (Composite)
small_box = Box('Small Box')
small_box.add(book)
small_box.add(ring)

# Big Box (Composite)
big_box = Box('Big Box')
big_box.add(watch)
big_box.add(pen)
big_box.add(small_box)

# Client
big_box.open()

"""
Advantage of Composite Design Pattern :
-> Create Complex Hierarchy (Tree Structure): এই প্যাটার্নের মাধ্যমে Tree-এর মতো Complex Hierarchy তৈরি করা যায়। যেমন— folder-এর ভেতর 
folder, তার ভেতর আরও folder এবং file। এটি data সাজানোর কাজকে অনেক সহজ করে দেয়।

-> Uniformity : এটি Leaf এবং Composite—উভয় object-কেই একইভাবে treat করার সুবিধা দেয়। client কে আলাদা করে check করতে হয় না যে সে 
কি একটি individual object(Watch) নিয়ে কাজ করছে নাকি একটি Container(Box) নিয়ে।

-> Simplified Client Code
client কোডে বারবার if-else বা switch-case ব্যবহার করে type check করার প্রয়োজন পড়ে না। client শুধু top level command দেয় 
(যেমন: open()), আর System নিজে থেকেই child গুলোর ভেতর recursively কাজটি সম্পন্ন করে।

-> Recursive Processing
পুরো একটি Object Tree ওপর কোনো Operation চালানো খুব সহজ হয়ে যায়। যেমন—পুরো বড় Box টির মোট দাম বের করা বা সবগুলো item একসাথে display করা।
"""
