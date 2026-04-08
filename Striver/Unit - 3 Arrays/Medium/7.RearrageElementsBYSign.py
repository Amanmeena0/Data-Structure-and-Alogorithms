from typing import List
class Solution:
    
    #Brute Force approach 
    def rearrangeArray1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        N = []
        P = []
        
        for num in nums:
            if num > 0:
                P.append(num)
                
            else:
                N.append(num)             
                
        Result = []
        for i in range(len(P)):
            Result.append(P[i])
            Result.append(N[i])
        return Result
    
    #Optimized Approach
    def rearrangeArray2(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        Result= [0]*n
        pos = 0
        neg = 1

        for i in range(n):

            if nums[i] > 0:
                Result[pos] = nums[i]
                pos += 2

            else:
                Result[neg] = nums[i]
                neg +=2

        return Result
        

    #more Optimized Version - but Not for every test case
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos = 0
        neg = 1
        n = len(nums)

        while(pos < n and neg < n):
            if nums[pos] >= 0: pos += 2
            elif nums[neg] < 0: neg += 2
            else:
                temp = nums[pos]
                nums[pos] = nums[neg]
                nums[neg] = temp
        
        return nums 
        
def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.rearrangeArray(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()