from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], k:int)-> int:
        
        sum = 0
        n = len(nums)
        
        for i in range(n):
            
            for j in range(i+1, n):

                if nums[i] + nums[j] == k:

                    return [i,j]
        return -1
    
    def TwoSum(self, nums: List[int], target:int) ->int:

        HashMap = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]

            if complement in HashMap:
                return (HashMap[complement], i)
            
            HashMap[nums[i] ] = i

        return -1
        
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the number: "))
    print(sol.longestSubarray(array,k))
    

if __name__ == "__main__":
    main()