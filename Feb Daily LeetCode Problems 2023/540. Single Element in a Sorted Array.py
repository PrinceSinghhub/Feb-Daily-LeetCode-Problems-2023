class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
          l = 0
          r = len(nums)-1
          while l<r:
              mid = (l+r)//2
              if mid%2 != 0:
                      if nums[mid] == nums[mid+1]:
                          r = mid
                      else:
                          l = mid+1
              else:
                      if nums[mid] == nums[mid+1]:
                          l = mid+1
                      else:
                          r = mid
          return nums[l]
