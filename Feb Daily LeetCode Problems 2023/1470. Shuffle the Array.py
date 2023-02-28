class Solution:
    def shuffle(self, nums, n):
        f = 0
        l = n
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(nums[f])
                f += 1
            else:
                res.append(nums[l])
                l += 1

        return res

