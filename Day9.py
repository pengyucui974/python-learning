# list_1=[]
# list_1.append([])
# list_1.append([])
# print(list_1)
# str_1="apple"
# print(sorted(str_1))

# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         sees=[]
#         sees_dict={}
#         strs_dict={}
#         answer=[]
#         num=0
#         for i in strs:
#             strs_dict[i]=sorted(i)
#             if strs_dict[i] not in sees or strs_dict[i] == "":
#                 sees.append(strs_dict[i])
#                 sees_dict[num]=[i]
#                 num+=1
#             else:
#                 for j in range(len(sees)):
#                     if sees[j] == strs_dict[i]:
#                         sees_dict[j].append(i)
#         for j in sees_dict:
#             answer.append(sees_dict[j])
#         return answer
#
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# solution = Solution()
# print(solution.groupAnagrams(strs))

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sees_dict={}
        strs_dict={}
        answer=[]
        for i in strs:
            strs_dict[i]="".join(sorted(i))
            if strs_dict[i] not in sees_dict:
                sees_dict[strs_dict[i]]=[i]
            else:
                sees_dict[strs_dict[i]].append(i)
        for j in sees_dict:
            answer.append(sees_dict[j])
        return answer

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs=["",""]
solution = Solution()
print(solution.groupAnagrams(strs))

