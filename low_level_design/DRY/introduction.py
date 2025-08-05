"""
Link-1 : https://blog.algomaster.io/p/082450d8-0e7b-4447-a8dc-b7308e45f048

Link-2 : https://www.geeksforgeeks.org/software-engineering/dont-repeat-yourselfdry-in-software-development/

--> একই ধরনের কোড, লজিক বা তথ্য একাধিক স্থানে না লিখে, একটি জায়গায় লিখে বারবার ব্যবহার করা। এতে কোড হবে:
    * পরিষ্কার (Clean)
    * রক্ষণাবেক্ষণযোগ্য (Maintainable)
"""

# Without DRY

def calculate_regular_discount(total_amount):
    if total_amount > 100:
        discount = total_amount * 0.1  # 10% discount
        final_amount = total_amount - discount
        print(f"Regular Customer : Total = ${total_amount}, Discount = ${discount}, Final = ${final_amount}")
    else:
        print(f"Regular Customer : Total = ${total_amount}, No Discount Applied.")


def calculate_premium_discount(total_amount):
    if total_amount > 100:
        discount = total_amount * 0.15  # 15% discount
        final_amount = total_amount - discount
        print(f"Premium Customer : Total = ${total_amount}, Discount = ${discount}, Final = ${final_amount}")
    else:
        print(f"Premium Customer : Total = ${total_amount}, No Discount Applied.")


def calculate_vip_discount(total_amount):
    if total_amount > 100:
        discount = total_amount * 0.2  # 20% discount
        final_amount = total_amount - discount
        print(f"VIP Customer : Total = ${total_amount}, Discount = ${discount}, Final = ${final_amount}")
    else:
        print(f"VIP Customer : Total = ${total_amount}, No Discount Applied.")


calculate_regular_discount(150)
calculate_premium_discount(150)
calculate_vip_discount(150)

"""
Problem: The logic for checking the total amount and applying a discount is repeated in each function, violating 
DRY. If we need to change the discount threshold (e.g., from $100 to $200), we must update all three functions, 
increasing the risk of errors.

Using DRY, we can consolidate the repeated logic into a single function or structure, making the code more 
maintainable. Here's a refactored version using a dictionary to store discount rates and a single function 
to handle the logic.
"""

def calculate_discount(total_amount, customer_type, discount_rates):
    discount_rate = discount_rates.get(customer_type, 0)
    customer_label = customer_type.capitalize()

    if total_amount > 100:
        discount = total_amount * discount_rate
        final_amount = total_amount - discount
        print(f"{customer_label} customer: Total = ${total_amount}, Discount = ${discount}, Final = ${final_amount}")
    else:
        print(f"{customer_label} customer: Total = ${total_amount}, No Discount Applied.")


discount_rates = {
    "regular": 0.1,
    "premium": 0.15,
    "vip": 0.2
}

calculate_discount(150, "regular", discount_rates)
calculate_discount(150, "premium", discount_rates)
calculate_discount(150, "vip", discount_rates)
