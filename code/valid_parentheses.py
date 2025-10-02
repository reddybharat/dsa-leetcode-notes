def isValid_recursive(s: str) -> bool:
    """
    Method 1: Recursive Approach (Highest Complexity)
    
    Recursive solution that processes the string and removes valid pairs.
    Less efficient due to string operations but demonstrates recursive thinking.
    
    Time: O(n^2), Space: O(n) - due to string replacement operations
    """
    if not s:
        return True
    
    # Remove valid pairs
    original = s
    s = s.replace('()', '').replace('{}', '').replace('[]', '')
    
    # If no changes made, string is invalid
    if s == original:
        return False
    
    # Recursively check the remaining string
    return isValid_recursive(s)


def isValid(s: str) -> bool:
    """
    Method 2: Hash Map + Stack (Optimal)
    
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    
    A string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    
    Time: O(n), Space: O(n)
    """
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in mapping.values():  # Opening bracket
            stack.append(char)
        elif char in mapping:  # Closing bracket
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack


def isValid_alternative(s: str) -> bool:
    """
    Method 3: Direct Character Matching + Stack
    
    Alternative approach using direct character comparisons instead of hash map.
    Slightly more verbose but same time/space complexity.
    
    Time: O(n), Space: O(n)
    """
    stack = []
    
    for char in s:
        if char in '({[':  # Opening bracket
            stack.append(char)
        elif char in ')}]':  # Closing bracket
            if not stack:
                return False
            
            last_open = stack.pop()
            if (char == ')' and last_open != '(') or \
               (char == '}' and last_open != '{') or \
               (char == ']' and last_open != '['):
                return False
    
    return not stack


def isValid_counter(s: str) -> bool:
    """
    Method 4: Counter Approach (Lowest Complexity - Only works for single type of parentheses)
    
    This approach only works for problems with a single type of parentheses.
    For multiple types, we need the stack approach.
    
    Time: O(n), Space: O(1)
    """
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0


# Example usage:
# print(isValid("()"))        # Output: True
# print(isValid("()[]{}"))    # Output: True
# print(isValid("(]"))        # Output: False
# print(isValid("([)]"))      # Output: False
# print(isValid("{[]}"))      # Output: True

# Test all methods:
# test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}", "", "((()))", "([{}])"]
# for test in test_cases:
#     print(f"'{test}': {isValid(test)} | {isValid_alternative(test)} | {isValid_recursive(test)}")
