# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
def searchMatrix( matrix, target):
    m , n = len(matrix) , len(matrix[0])
    target_found= False
    for i in range (0,m):
        if target >= matrix[i][0]:
            for j in range(0,n):
                if matrix[i][j]==target:
                    target_found = True
    return target_found     


print(searchMatrix(matrix,target))