"""
首先，计算出整个数组的和sum，如果sum%p==0，那么不需要移除任何元素，返回0。

否则，我们需要找到最短的子数组，使得子数组的和% p == (sum%p)。 如果不存在这样的子数组，则返回-1。

为了找到最短的子数组，我们可以遍历数组，并计算每个位置的前缀和。 假设我们现在正在考虑位置i，即nums[0] + nums[1] + ... + nums[i]。 如果(i+1)%p==0，则整个数组可以被划分为两个子数组，第一个子数组的和为nums[0]+nums[1]+...+nums[i]，第二个子数组的和为nums[i+1]+nums[i+2]+...+nums[n-1]，它们的和为sum。 因此，我们只需要移除第二个子数组即可。

如果(i+1)%p!=0，则我们需要找到最短的子数组，使得子数组的和% p == (sum%p - prefix_sum[i+1]%p + p) % p。 我们可以使用哈希表来记录每个余数第一次出现的位置。 我们首先将哈希表初始化为{-1:0}，其中-1表示余数为0的情况，值为0表示空子数组的和为0。 我们遍历数组，并计算前缀和的余数。 如果当前余数已经在哈希表中出现过，则我们需要找到最短的子数组，使得子数组的和% p == (sum%p - prefix_sum[i+1]%p + prefix_sum[j]%p + p) % p，其中j是哈希表中余数为当前余数的最后一个位置。 因此，我们只需要移除从j+1到i的元素。 如果当前余数在哈希表中未出现，则将其加入哈希表。

在遍历数组时，我们可以使用一个变量min_length来记录最短的子数组的长度。 如果在遍历完成后min_length仍然为n，则说明不存在这样的子数组，返回-1。 否则，返回min_length。

作者：Haitao.Huang
链接：https://leetcode.cn/problems/make-sum-divisible-by-p/solutions/2159081/1590-shi-shu-zu-he-neng-bei-p-zheng-chu-en3vo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
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