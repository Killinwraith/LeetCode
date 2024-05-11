
def isValid(s):
    '''
    :type s: str
    :rtype: bool
    '''
 
    opening = {'(', '[', '{'}
    closing = {')': '(', ']': '[', '}': '{'}
    
    stack = []
    total = False
    if len(s) == 1:
        return False
    if s[0] in closing:
        return False

    for parenthesis in s:
        if parenthesis in opening:
            stack.append(parenthesis)
        elif parenthesis in closing:
            if len(stack) > 0:
                if stack.pop() != closing[parenthesis]:
                    return False
                else:
                    total = True
            else:
                total = False
    return total

print('Test 1: input = \'()\' - ',isValid('()'))
print('Test 2: input = \'((\' - ',isValid('(('))
print('Test 3: input = \'()[]{}\' - ',isValid('()[]{}'))
print('Test 4: input = \'(}\' - ',isValid('(}'))
print('Test 5: input = \'([)]\' - ',isValid('([)]')) 
print('Test 6: input = \'(){}}{\' - ',isValid('(){}}{')) 
