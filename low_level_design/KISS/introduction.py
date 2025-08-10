"""
Link-1: https://www.geeksforgeeks.org/software-engineering/kiss-principle-in-software-development/ (more Description)

Link-2: https://blog.algomaster.io/p/21b57678-b351-4ed4-b390-3b6308af2f7d
"""

def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    if not s:
        return True

    def clean_string(s):
        return ''.join(char.lower() for char in s if char.isalnum())

    def check_palindrome(s, left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return check_palindrome(s, left + 1, right - 1)

    cleaned = clean_string(s)
    return check_palindrome(cleaned, 0, len(cleaned)-1)

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("A Man Called Otto"))

""" Simple (KISS) Solution """

def check_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(check_palindrome("was it a car or a cat i saw"))
print(check_palindrome("fuck you.."))
