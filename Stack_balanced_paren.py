def is_match(p1,p2):
    if p1=="{" and p2=="}":
        return True
    elif p1=="(" and p2==")":
        return True
    elif p1=="[" and p2=="]":
        return True
    return False
def is_balanced(paren_string):
    stack = Stack()
