from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, array:List[int]) -> List[int]:
        
        res = []
        freq = Counter(array)
        n = len(array)
        n /= 3


        for key in freq:
            
            if freq[key] > n:
                res.append(key)
        

        return res

    def majorityElement(self, array:List[int]) -> List[int]:
        if not array:
            return []
        ele1 = 0
        ele2 = 1

        count1 = count2 = 0

        for ele in array:
            if ele == ele1:
                count1 += 1
            elif ele == ele2:
                count2 += 1 
            elif count1 == 0:
                ele1 = ele
                count1 = 1
            elif count2 == 0:   
                ele2 = ele
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        result = []
        n = len(array)
        for cand in [ele1, ele2]:
            if array.count(cand) > n // 3:
                result.append(cand)
        
        return list(set(result))
            




def main():

    sol = Solution()
    array = list(map(int, input("Enter numbers separated by spaces: ").split()))
    # k = int(input("Enter the number: "))
    print(sol.majorityElement(array))
    # sol.sortColors(array)
    # for i in array:
    #     print(i, end=" ")

if __name__ == "__main__":
    main()