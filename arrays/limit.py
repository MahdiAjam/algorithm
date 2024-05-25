"""
Sometimes you need to limit array result to use. Such as you only need the
 value over 10 or, you need value under than 100. By use this algorithm, you
 can limit your array to specific value

If array, Min, Max value was given, it returns array that contains values of
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.

Complexity = O(n)
"""

def limit(arr, min=None, max=None):

    min_check = lambda val: True if min is None else (val >= min)
    max_check = lambda val: True if max is None else(val <= max)

    return [val for val in arr if min_check(val) and max_check(val)]

print(limit([1, 2, 3, 4, 5, 6, 7, 8, 9], min=5, max=5))


'''in another way '''

'''
def limit(arr, min=None, max=None):
    check = []

    if max and min:
        check.append(max)

    elif min:
        for val in arr:
            if val >= min:
                check.append(val)

    elif max:
        for val in arr:
            if val <= max:
                check.append(val)
                
    print(check)

limit([1, 2, 3, 4, 5, 6, 7, 8, 9], min=5, max=5)
'''