# encoding=utf-8
'''
题目:https://leetcode.com/problems/two-sum
'''

class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_list = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == target:
                    tmp_list.append(i)
                if target == nums[i] + nums[j]:
                    return [i, j]
        return tmp_list

    def run(self):
        nums = [0, 4, 3, 0]
        target = 0
        res = self.two_sum(nums, target)
        print res


if __name__ == '__main__':
    Solution().run()
