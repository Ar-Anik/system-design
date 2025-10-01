"""
1. Telescoping Constructor Problem কী?
-> যখন কোনো ক্লাসে অনেকগুলো optional parameter থাকে, তখন সেগুলো হ্যান্ডেল করার জন্য আমরা অনেকগুলো constructor (অর্থাৎ
overloaded constructor) তৈরি করি। কিন্তু constructor-এ তো default মান (যেমন Python ফাংশনে থাকে param=False) দেওয়া যায় না।
ফলে আমাদের একটার ভেতরে আরেকটা constructor কল করতে হয়, আর constructor গুলো ধাপে ধাপে লম্বা হতে হতে "টেলিস্কোপ" এর মতো বড় হয়।
এটাকেই বলে Telescoping Constructor Problem।

Builder Pattern ব্যবহার করে, Telescoping constructor problem সমাধান করতে পারি।
"""

"""
# Telescoping Constructor Problem in Java

public class Pizza {
    private int size;
    private boolean cheese;
    private boolean pepperoni;
    private boolean bacon;
    private boolean mushrooms;

    // শুধু size
    public Pizza(int size) {
        this(size, false);
    }

    // size + cheese
    public Pizza(int size, boolean cheese) {
        this(size, cheese, false);
    }

    // size + cheese + pepperoni
    public Pizza(int size, boolean cheese, boolean pepperoni) {
        this(size, cheese, pepperoni, false);
    }

    // size + cheese + pepperoni + bacon
    public Pizza(int size, boolean cheese, boolean pepperoni, boolean bacon) {
        this(size, cheese, pepperoni, bacon, false);
    }

    // সব option
    public Pizza(int size, boolean cheese, boolean pepperoni, boolean bacon, boolean mushrooms) {
        this.size = size;
        this.cheese = cheese;
        this.pepperoni = pepperoni;
        this.bacon = bacon;
        this.mushrooms = mushrooms;
    }
}
"""

"""
-> Java / C++–এ constructor overloading করতে হয়, আর default argument  system নেই (Java-তে নেই, C++-এ limited ভাবে আছে)। 
ফলে আলাদা আলাদা constructor লিখতে হয়, আর যত optional parameter বাড়ে,  constructor গুলো তত লম্বা বা “টেলিস্কোপের মতো” হয়।

-> Python-এ Telescoping Constructor Problem নেই, Python-এ __init__ মেথড একবারই লিখি। আমরা সহজে default parameter সেট 
করতে পারি।
"""


"""
-> Builder Pattern ব্যবহার করে কোনো জটিল অবজেক্ট (যেমন Composite Tree, Graph, Document ইত্যাদি) খুব সহজে step-by-step তৈরি করা যায়

1. Step-by-step construction
- Builder দিয়ে একটা প্রোডাক্ট এক ধাপে না বানিয়ে ধাপে ধাপে তৈরি করা হয়।
- যেমন: আগে root বানানো → তারপর child যোগ করা → তারপর তাদের sub-child যোগ করা।

2. Deferred execution (কিছু ধাপ পরে করা যায়)
- সব ধাপ একসাথে না করলেও Builder কাজ করবে। প্রয়োজন অনুযায়ী কিছু ধাপ পরে চালাতে পারবো, কিন্তু final product ঠিকঠাক তৈরি হবে।

3. Recursive building
- Tree/Graph-এর মতো স্ট্রাকচার বানাতে recursive step দরকার হয়। Builder এটা খুব সহজে হ্যান্ডেল করতে পারে।

4. Incomplete product expose না করা
- object create complete না হওয়া পর্যন্ত ক্লায়েন্ট কোড সেটাতে অ্যাক্সেস করতে পারে না। শুধু build() করার পরেই পুরো অবজেক্ট রিটার্ন হয়।
"""