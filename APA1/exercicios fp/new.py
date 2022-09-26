# Given a string s and a string t, return a string in which all the characters 
# of s that occur in t have been replaced by a  sign. The comparisons are 
# case sensitive.

def replaceCharactersWithUnderscores(s, t):
    result = ""

    for c in s:
        if c in t:
            result += ""
        else:
            result += c

    return result
# Given a string s, return the longest prefix that is repeated somewhere else in the string.
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
    if len(s) == 0:
        return ""

    prefix = s[0]

    for i in range(1, len(s)):
        newPrefix = prefix + s[i]
        if newPrefix in s[len(newPrefix):]:
            prefix = newPrefix
        else:
            break

    if len(prefix) == 1 and prefix not in s[1:]:
        return ''

    return prefix
# Given a string s, return the longest prefix that is repeated somewhere else in the string.
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
    if len(s) == 0:
        return ""

    prefix = s[0]

    for i in range(1, len(s)):
        newPrefix = prefix + s[i]
        if newPrefix in s[len(newPrefix):]:
            prefix = newPrefix
        else:
            break

    if len(prefix) == 1 and prefix not in s[1:]:
        return ''

    return prefix