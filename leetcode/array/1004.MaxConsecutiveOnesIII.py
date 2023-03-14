"""
主要思路是维护一个滑动窗口，该窗口内最多可以翻转k个0。用flip记录当前窗口内需要翻转的0的个数。
如果flip大于k，说明窗口中需要翻转的0的个数已经超过k，需要从左边开始，将需要翻转的0翻转为1，将左端点left向右移动一格。
因为左端点为left的窗口已经不再合法，从而不会影响后续计算。最后统计窗口内1的个数并更新最长的1序列长度。
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0    # 左指针
        ans = 0     # 最终答案
        flip = 0    # 记录需要翻转的0的个数
        for right, x in enumerate(nums):   # 枚举右端点
            flip += 1 - x   # 统计需要翻转的0的个数
            while flip > k: # 如果需要翻转的0的个数大于k
                flip -= 1 - nums[left]  # 从左边开始，将需要翻转的0翻转为1
                left += 1   # 左指针向右移动一格，因为左端点为left的窗口不再合法
            ans = max(ans,right - left + 1)  # 更新最长的1序列长度
        return ans

                