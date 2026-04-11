from typing import List

class Solution:
    # Brute Force Approach
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = 0
        

        for i in range(len(nums)):
            sum = 0
            
            for j in range(i, len(nums)):
                
                sum += nums[j]
                if sum == k:
                    n += 1

        return n
    

    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_count = defaultdict(int)
        prefix_count[0] = 1   # important base case
        
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            
            if (curr_sum - k) in prefix_count:
                count += prefix_count[curr_sum - k]
            
            prefix_count[curr_sum] += 1
        
        return count      


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