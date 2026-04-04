from typing import List

class Solution:

    #brute force approach 
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        MaxOnes = 0    
        ones = 0
        for i in range(len(nums)):

            if(nums[i] == 1):
                ones+=1
            else:
                ones = 0

            MaxOnes =  max(MaxOnes, ones)
        return MaxOnes
            
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))

    print(sol.findMaxConsecutiveOnes(array))
    

if __name__ == "__main__":
    main()