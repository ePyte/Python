class Permutation:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res, oneSol = [], []

        def backtrack():
            if (len(oneSol) == n):
                res.append(oneSol[:])
                return
            
            for element in nums:
                if element not in oneSol:
                    oneSol.append(element)
                    backtrack()
                    oneSol.pop()

        backtrack()
        return res

#Demonstration and tests

print("Example1:")
first_P = Permutation()
print(first_P.permute([1, 2, 3]))
first_Sol = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print("Test1:")
print(first_P.permute([1, 2, 3]) == first_Sol)


print("Example2:")
second_P = Permutation()
print(second_P.permute([0, 2, 4, 6]))
second_Sol = [[0, 2, 4, 6], [0, 2, 6, 4], [0, 4, 2, 6], [0, 4, 6, 2], [0, 6, 2, 4], [0, 6, 4, 2], [2, 0, 4, 6], [2, 0, 6, 4], [2, 4, 0, 6], [2, 4, 6, 0], [2, 6, 0, 4], [2, 6, 4, 0], [4, 0, 2, 6], [4, 0, 6, 2], [4, 2, 0, 6], [4, 2, 6, 0], [4, 6, 0, 2], [4, 6, 2, 0], [6, 0, 2, 4], [6, 0, 4, 2], [6, 2, 0, 4], [6, 2, 4, 0], [6, 4, 0, 2], [6, 4, 2, 0]]
print("Test2:")
print(second_P.permute([0, 2, 4, 6]) == second_Sol)

