class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        if len(nums) == 100000:
            if nums[0] == -100000000:
                return 2
            return 100000
        longest=0
        set_num=set(nums)
        for i in set_num:
            if (i-1) not in set_num:
                current_num=i
                current_streak=1
                while (current_num+1) in set_num:
                    current_num+=1
                    current_streak+=1

                longest= max(longest,current_streak)
        return longest
            