def isValid_2(s):
    """
    :type s: str
    :rtype: bool
    """
    open = '({['
    close = ')}]'
    tmp = []
    for ch in s:
        if ch in open:
            tmp.append(close[open.index(ch)])
        elif tmp:
            if ch == tmp.pop():
                continue
            else:
                return False
        else:
            return False
    if tmp:
        return False
    return True


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    par = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    tmp = []
    for ch in s:
        if ch in par:
            if tmp and tmp[-1] == par[ch]:
                tmp.pop()
            else:
                return False
        else:
            tmp.append(ch)
    if tmp:
        return False
    return True

print(isValid_2("()"))
print(isValid_2("()[]{}"))
print(isValid_2("]()[]{}"))
print(isValid_2("(]"))
print(isValid_2("()]{}"))
print(isValid_2("()]"))
