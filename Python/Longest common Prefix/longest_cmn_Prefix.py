def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    min_length = min(len(s) for s in strs)
    prefix = ""

    for i in range(min_length):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break
    
    return prefix


print(longestCommonPrefix(["flower","flow","flight"]))

