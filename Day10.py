class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_sorted = sorted(list(set(nums)))
        if len(list_sorted)>0:
           real_max_length = 1
        else:
            real_max_length = 0
            return real_max_length
        i=0
        while True:
            max_length = 1
            print(i)
            while True:
                if list_sorted[i] + 1 in list_sorted:
                    i+=1
                    max_length += 1
                else:
                    i+=1
                    break
            if max_length >real_max_length:
                real_max_length = max_length
            if real_max_length>=(len(list_sorted)-i):
               break
        return real_max_length

nums=[]
sol=Solution()
print(sol.longestConsecutive(nums))