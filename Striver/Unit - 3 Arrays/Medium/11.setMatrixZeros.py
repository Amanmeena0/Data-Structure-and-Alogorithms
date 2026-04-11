from typing import List
class Solution:
    #brute force approach
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix) 
        n = len(matrix[0])
        temp = [row[:] for row in matrix]

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0:

                    for k in range(n):
                        temp[i][k] = 0

                    for k in range(m):
                        temp[k][j] = 0

        for i in range(m):
            for j in range(n):
                matrix[i][j] = temp[i][j]


    #better approach
    def setZeroes1(self, matrix: List[List[int]]) -> None:
        m = len(matrix) 
        n = len(matrix[0])

        row = [False]*m
        col = [False]*n

        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(m):
            for j in range(n):

                if row[i] == True or col[j] == True:

                    matrix[i][j] = 0

    #optimal approch 
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
        
        if firstRowZero :
            for j in range(n):
                matrix[0][j] = 0

def main():

    sol = Solution()
    R = int(input("Enter the number of Rows: "))
    C = int(input("Enter the number of Cols: "))
    array = [list(map(int, input("Enter num_setbers separated by spaces: ").split())) for _ in range(R)]
    # k = int(input("Enter the num_setber: "))
    # print(sol.longestConsecutive(array))
    sol.setZeroes(array)
    for i in range(R):
        for j in range(C):
            print(array[i][j], end=" ")
        print(end=" ")

if __name__ == "__main__":
    main()