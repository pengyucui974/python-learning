#Leetcode No.283
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         i = 0
#         num_zeros = 0
#         flag = True
#         while True:
#             if i == len(nums):
#                 break
#             if nums[i] == 0:
#                 j = i
#                 while True:
#                     if nums[j] == 0:
#                         j += 1
#                         if j == len(nums):
#                             flag = False
#                             break
#                         else:
#                             num_zeros += 1
#                     else:
#                         break
#                 if flag == True:
#                     value = nums[j]
#                     nums[j] = nums[j - num_zeros]
#                     nums[j - num_zeros] = value
#                     i = j + 1
#                 else:
#                     break
#             else:
#                 value = nums[i]
#                 nums[i] = nums[i - num_zeros]
#                 nums[i - num_zeros] = value
#                 i = i + 1
#         return nums

class Solution(object):
    def moveZeroes(self, nums):
        slow = 0  # 下一个非零元素应该放的位置

        for fast in range(len(nums)):  # 检查每个元素
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums


sol=Solution()
nums = [0,1,0,3,1,2]
# nums=[0]
print(sol.moveZeroes(nums))