# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#  Example 1:
#     Input: x = 4
#     Output: 2
# Example 2:
#     Input: x = 8
#     Output: 2

#using binary search 
def sqrts(x):
    if x < 2:
        return x
    
    left , right = 0 , x//2
    res = 1 

    while left <= right :
        mid = (left + right)//2

        if mid * mid == x:
            return mid 
        elif mid * mid < x :
            res = mid 
            left = mid + 1
        else : right = mid - 1

    return res


n = int(input("Enter any Number : "))
root = sqrts(n)
print(root)