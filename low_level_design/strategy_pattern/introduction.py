"""
Link-Bangla : https://medium.com/প্রোগ্রামিং-পাতা/strategy-design-pattern-স্ট্র্যাটেজি-ডিজাইন-প্যাটার্ন-6def99bc5407/ (Code Example-1)

Link-2 : https://refactoring.guru/design-patterns/strategy

Link-3 : https://www.geeksforgeeks.org/system-design/strategy-pattern-set-1/#when-not-to-use-the-strategy-design-pattern (Too much describe same shit)

-> The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets
the algorithm vary independently from clients that use it.

-> একই ধরনের একাধিক অ্যালগরিদম বা কৌশলকে একটি family হিসেবে define করে, প্রতিটিকে আলাদাভাবে encapsulate করে, এবং একে অপরের বিকল্প হিসেবে
ব্যবহারযোগ্য করে তোলে। এইভাবে, মূল ক্লাস (যে ক্লাস অ্যালগরিদম ব্যবহার করে) কে পরিবর্তন না করেই অ্যালগরিদমগুলো সহজে পরিবর্তন বা আপডেট করা যায়। এতে
অ্যালগরিদম ও ব্যবহারের অংশ (client) আলাদা থেকে স্বাধীনভাবে কাজ করতে পারে।

-> স্ট্রাটেজি (Strategy) একটি Behavioral Design Pattern যা আপনাকে একটি অ্যালগরিদমের পরিবারের (family of algorithms) সংজ্ঞা দিতে, প্রতিটিকে
আলাদা ক্লাসে রাখতে এবং তাদের অবজেক্টগুলোকে একে অপরের পরিবর্তে ব্যবহারযোগ্য (interchangeable) করতে সাহায্য করে।
অর্থাৎ, আপনি একই কাজ করার জন্য একাধিক ভিন্ন পদ্ধতি তৈরি করতে পারেন, এবং রানটাইমে প্রয়োজন অনুযায়ী যেকোনো একটি পদ্ধতি বেছে নিয়ে ব্যবহার করতে
পারেন — কোড পরিবর্তন না করেই।

-> The Strategy Pattern lets us define a family of methods or algorithms, put each one into its own class, and make these
classes interchangeable inside the code that uses them. This way, we can change the behavior of our program without
changing its structure.
"""

"""
> Parts of the Strategy Pattern (Full Version)
1. Strategy (Interface or Abstract Class)
Declares the algorithm interface.

2. Concrete Strategies
Implement the algorithm declared in the Strategy.

3. Context
Holds a reference to a Strategy object. Uses the Strategy object to execute the algorithm.

4. Client
Creates and configures the Context. Chooses which Concrete Strategy the Context should use. Can 
swap the strategy at runtime if needed.

> Flow of Use
    * Client decides which algorithm to use.
    * Client passes the chosen algorithm (Concrete Strategy) to the Context.
    * Context calls the algorithm through the Strategy interface — it doesn’t know which specific one is used.
    * Algorithm (Concrete Strategy) executes and returns the result to the Context.
"""
