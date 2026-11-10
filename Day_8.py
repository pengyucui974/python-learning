# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         total=0
#         len_nums=len(nums)
#         for i in range(len_nums):
#             for j in range(i+1,len_nums):
#                 total=i+j
#                 if total == target:
#                     answer=[i,j]
#                     print(answer)
#                     return answer


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens_num=len(nums)
        checked={}
        for i in range(lens_num):
            complement=target-nums[i]
            if complement in checked:
                return [i,checked[complement]]
            else:
                checked[nums[i]]=i
nums=[3,2,4]
target=6
solution = Solution()
print(solution.twoSum(nums,target))