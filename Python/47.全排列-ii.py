#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def backtrack(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return


# @lc code=end
