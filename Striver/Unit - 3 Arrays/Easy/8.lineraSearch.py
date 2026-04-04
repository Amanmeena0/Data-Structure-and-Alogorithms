from typing import List

class Solution:

    #brute force approach 
    def linearSearch(self, nums: List[int], n:int) -> int:

        for i in range(len(nums)):
            if n == nums[i]:
                return 1
        
        return -1
            
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter the number you want to find: "))
    print(sol.linearSearch(array,target))
    

if __name__ == "__main__":
    main()