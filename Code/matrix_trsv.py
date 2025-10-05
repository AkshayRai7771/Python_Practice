#spiral traverse 
# mat= [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# m,n = len(mat),len(mat[0])
# ans = []
# top,bottom = 0,m-1
# left,right = 0,n-1
# while top<=bottom and left<=right:
#     for i in range(left,right+1):
#         ans.append(mat[top][i])
#     top+=1
    
#     for i in range(top,bottom+1):
#         ans.append(mat[i][right])
#     right-=1
#     if top<=bottom:
#         for i in range(right,left-1,-1):
#             ans.append(mat[bottom][i])
#     bottom-=1
#     if left<=right:
#         for i in range(bottom,top-1,-1):
#             ans.append(mat[i][left])
#     left+=1


#transpose of matrix
matrix = [[1,2,3],[4,5,6]]

m,n = len(matrix),len(matrix[0])
matrix1 = [[None]*m for _ in range(n)]
for i in range(0,n):
    for j in range(0,m):
        matrix1[i][j]= matrix[j][i]
print(matrix1)


