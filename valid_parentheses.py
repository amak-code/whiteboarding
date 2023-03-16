# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# ] , { , }, [
def is_valid(s):

    parentheses = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    seen = [] #this list is used for left parentheses

    for ch in s:
        if ch not in parentheses and not seen:
            return False
        
        else:
            if ch in parentheses:
                seen.append(ch)
            else:
                if parentheses.get(seen.pop()) != ch:
                    return False
                
    return seen == []


print(is_valid(")[]("))