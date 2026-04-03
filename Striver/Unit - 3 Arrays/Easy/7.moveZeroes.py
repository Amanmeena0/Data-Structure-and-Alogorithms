from typing import List

class Solution:

    #brute force approach 
    def moveZeroes(self, nums: List[int]) -> None:

        j = 0
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
    
        
    
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    sol.moveZeroes(array)
    
    for num in array:
        print(num,end=" ")

if __name__ == "__main__":
    main()
