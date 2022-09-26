# Given a list of integers, return the difference of the positions
# of the first and last occurence of the largest element,
# You may assume that the largest element occurs at least once,
# You may also assume that the given list contains at least one
# element. Do not use builtins min, max, find or index.


def positionDifferenceFirstLastLargest(arr):
    assert len(arr) >= 1
    maximum = arr[0] # let's assume the biggest number is the first one, so we can check if there are bigger numbers in the list
    indexList = [] # list of indexes of the higest value
    for i in range(len(arr)):
        if maximum < arr[i]:
            maximum = arr[i]
    for n in range(len(arr)):
        if arr[n] == maximum:
            indexList.append(n)
    difference = indexList[0] - indexList[-1]
    return difference
    # OUTRO METODO:
   # maximum = arr[0]
   # for num in arr:
   #     print(num)
   #     if num > maximum:
   #        maximum = num
   # return maximum


list1 = [1,569,12035,1230,12035, 12035, 11,23, 12035]
list2 = [-1,-10,105,1,20,5]

print(positionDifferenceFirstLastLargest(list1))
# print(positionDifferenceFirstLastLargest(list2))