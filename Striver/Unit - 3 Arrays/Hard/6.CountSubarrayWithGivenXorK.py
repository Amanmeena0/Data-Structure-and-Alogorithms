from typing import List


class Solution:
    def subarraysWithXorK(self,arr:List[int], k : int)->int:
        
        count = 0

        for i in range(len(arr)):

            for j in range(i, len(arr)):

                

        return 

def main():
    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the integer: "))
    print(sol.subarraysWithXorK(array))

    
if __name__ == "__main__":
    main()
