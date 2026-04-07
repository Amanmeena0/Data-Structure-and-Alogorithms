from typing import List

class Solution:
    def sortColors(self, nums: List[int]):
        FinalSum = float('-inf')
        Sum = 0 
        Start = 0
        subArray = []

        for end in range(len(nums)):

            Sum += nums[end]
            
            if Sum > FinalSum:
                FinalSum = Sum
                subArray = nums[Start:end+1]

            if Sum < 0:
                Sum = 0
                Start = end + 1


        return FinalSum, subArray
        
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.sortColors(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()