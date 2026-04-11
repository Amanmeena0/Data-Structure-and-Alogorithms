from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0]) 

        num = []

        top = 0
        left = 0
        bottom = row - 1
        right = col - 1

        while top <= bottom and left <= right:

            for i in range(left, right+1):
                num.append(matrix[top][i])
            top+=1

            for i in range(top, bottom+1):
                num.append(matrix[i][right])
            right-=1 

            if top <= bottom:
                for i in range(right, left-1,-1):
                    num.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1,-1):
                    num.append(matrix[i][left])
                left += 1


        return num
        
        

            


def main():

    sol = Solution()
    array = list(map(int, input("Enter num_setbers separated by spaces: ").split()))
    # k = int(input("Enter the num_setber: "))
    print(sol.spiralOrder(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()