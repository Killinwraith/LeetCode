
def isValid(s):
    '''
    :type s: str
    :rtype: bool
    '''
    total = True
    stack = []
    parenthesis = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    for i in s:
        if i in parenthesis.values():
            stack.append(i)
        else:
            # If ( stack is not empty ) or the last item in stack != parenthesis then cut
            if not stack or stack.pop() != parenthesis[i]:
                return False

    if stack:
        return False
    
    return total

print('Test 1: [True] input = \'()\' - ',isValid('()'))
print('Test 2: [False] input = \'((\' - ',isValid('(('))
print('Test 3: [True] input = \'()[]{}\' - ',isValid('()[]{}'))
print('Test 4: [False] input = \'(}\' - ',isValid('(}'))
print('Test 5: [False] input = \'([)]\' - ',isValid('([)]')) 
print('Test 6: [False] input = \'(){}}{\' - ',isValid('(){}}{')) 
