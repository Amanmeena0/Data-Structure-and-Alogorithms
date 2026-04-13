from typing import List

class Solution:
    def generate(self, numRows:int) -> List[List[int]]:
        triangle = [[1]]
        
        for i in range(numRows- 1):

            temp = [0] + triangle[-1] + [0]

            row = []

            for j in range(len(triangle[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            
            triangle.append(row)

        return triangle




def main():

    sol = Solution()
    # array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the number: "))
    print(sol.generate(k))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()