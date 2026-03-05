class Solution:
    def countFrequencies(self, nums):
        freq = {}

       
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = []
        for key, value in freq.items():
            result.append([key, value])

        return result

if __name__ == "__main__":
    sol = Solution()

    n =  [5, 5, 5, 5]
    result = sol.countFrequencies(n)

    print(result)