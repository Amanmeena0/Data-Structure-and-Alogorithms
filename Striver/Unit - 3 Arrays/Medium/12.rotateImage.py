from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])



        for i in range(m):            
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(m):
            matrix[i].reverse()


def main():

    sol = Solution()
    array = list(map(int, input("Enter num_setbers separated by spaces: ").split()))
    # k = int(input("Enter the num_setber: "))
    print(sol.rotate(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()