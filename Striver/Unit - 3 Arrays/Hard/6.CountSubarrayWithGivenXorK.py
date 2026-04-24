from typing import List
class Solution:
    def SubarraysWithXorK(self,arr:List[int], k : int)->int:
        
        count = 0
        for i in range(len(arr)):
            xored = 0

            for j in range(i, len(arr)):
                
                xored ^= arr[j]

                if xored ==  k:
                    count +=1            

        return count 

    #using prefix Sum
    def SubarraysWithXorK1(self, arr: List[int], k:int)->int:

        res = 0
        current_xor = 0
        freq = {}
        freq = {0:1}

        for num in arr:

            current_xor ^= num

            target = current_xor ^ k

            if target in freq:

                res += freq[target]

            freq[current_xor] = freq.get(current_xor,0) + 1

        return res
    
    #{4, 2, 2, 6, 4},D k = 6, output = 4   
def main():
    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter the integer: "))
    print(sol.SubarraysWithXorK(array,k))

    
if __name__ == "__main__":
    main()
