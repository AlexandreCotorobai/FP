# coordenadas.py

# Write a function that checks whether two points with coordinates 
# x1, y1 and x2, y2 are in the same quadrant. The given coordinates 
# will not be on the x- or y-axis.

def coordinatesInSameQuadrant(x1, y1, x2, y2):
    result = ""
    if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0: # first quadrant
        result = "First Quadrant"
    #elif...

# Given numbers x, y, and target, return whichever of x and y is closer 
# to the target. If they have the same distance, return the smaller of the two.

def closer(x, y, target):
    if abs(target - x) > abs(target - y):
        return y
    elif abs(target - x) < abs(target - y):
        return x
    else:
        return min(x,y)

# Given a list of integers and an integer n, return 
# a list of the averages of n consecutive elements of the original list.
# You may assume there is at least one element in the given list.

def average(arr, n):
    if len(arr) == 0 or n > len(arr):
        return None
    
    avgs = []
    for i in range(2, n+1):
        avgs.append(sum(arr[:i]) / i)

    return avgs

print(average([5,10,15,20], 4))

# Given a string s and a string t, return a string in which all the characters 
# of s that occur in t have been replaced by a  sign. The comparisons are 
# case sensitive.

def occurrences(s,t):
    new_string = ""
    for char in s:
        if char in t:
            new_string += "-"
        else:
            new_string += char
    
    return new_string

print(occurrences("abcdfegasjkldghawodhl", "abcdefgdgjklnertgh"))

# Given a string s, return the longest prefix that is repeated somewhere else in the string.
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def prefix(s):
    longest_prefix = ""
    for i in range(len(s)):
        if s[:i] in s[i:]:
            longest_prefix = s[:i]
        else:
            break
    
    return longest_prefix

print(prefix("abcsldjhfgweio4gh abcs"))