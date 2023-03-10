class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        # 求数组中所有元素的和，并对p取余，得到目标值
        target = sum(nums) % p
        # 如果目标值为0，则整个数组都可以被p整除
        if target == 0:
            return 0
        # 初始化哈希表，key为余数，value为最后一次出现该余数的下标
        remainders = {0: -1}
        remainder = 0
        min_length = n
        for i in range(n):
            # 求前缀和，并对p取余，得到当前余数
            remainder = (remainder + nums[i]) % p
            # 将当前余数记录到哈希表中，保证哈希表中存储的是最后一次出现该余数的下标
            remainders[remainder] = i
            # 如果当前余数减去目标值的余数在哈希表中出现过，则更新最小子数组的长度
            if (remainder - target) % p in remainders:
                j = remainders[(remainder - target) % p]
                min_length = min(min_length, i - j)

        # 如果最小子数组的长度为n，则无法满足题目要求，返回-1
        return -1 if min_length == n else min_length