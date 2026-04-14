from typing import List

class Solution:
    def threeSum(self, numRows:int) -> List[List[int]]:
        ans = [[]]

             
        return ans




def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.threeSum(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()