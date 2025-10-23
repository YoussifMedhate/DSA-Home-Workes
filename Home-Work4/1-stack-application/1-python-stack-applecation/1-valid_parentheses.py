from collections import deque

def check_parentheses(expression: str) -> bool:
    """Checks if all parentheses and brackets are balanced."""
    
    stk = deque()
    pairs = {')': '(', ']': '[', '}': '{'} 
    
    for ch in expression:
        if ch in pairs.values():
            stk.append(ch)
        elif ch in pairs:
            if not stk or stk.pop() != pairs[ch]:
                return False
    
    return not stk
