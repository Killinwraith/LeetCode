
def isValid(s):
    '''
    :type s: str
    :rtype: bool
    '''
 
    stack = []
    total = False
    if len(s) == 1:
        return False
    
    for letter in s:
        if letter in ("(","{","["):
            stack.append(letter)
        else:
            firstToClose = stack.pop()
            if (letter == (")") and firstToClose == ("(")) or (letter == ("}") and firstToClose == ("{")) or (letter == ("]") and firstToClose == ("[")):
                total = True
            else:
                return False
    
    return total

"""
currenlty failling....I need to fix this some how ....
"""

print('Test 1: input = \'()\' - ',isValid('()'))
print('Test 1: input = \'((\' - ',isValid('(('))
print('Test 2: input = \'()[]{}\' - ',isValid('()[]{}'))
print('Test 3: input = \'(}\' - ',isValid('(}'))
print('Test 4: input = \'([)]\' - ',isValid('([)]'))
