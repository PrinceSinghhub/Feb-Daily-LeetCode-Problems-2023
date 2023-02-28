class Solution:
    def searchInsert(self, nums, target):

        start = 0
        end = len(nums)

        while (start < end):

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid
            if nums[mid] < target:
                start = mid + 1
        return start

