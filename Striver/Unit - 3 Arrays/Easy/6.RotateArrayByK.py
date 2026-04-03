from typing import List

class Solution:

    #brute force approach 
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k %= n
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)

    #optimized version
    def rotate1(self, nums: List[int], k: int) -> None:    
        
        n = len(nums)
        k %= n
        
        nums.reverse()
        nums[0:k] = nums[0:k][::-1]
        nums[k:n] = nums[k:n][::-1]
            
        
    
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the K: "))
    sol.rotate1(array,k)
    
    for num in array:
        print(num, end=" ")

if __name__ == "__main__":
    main()
