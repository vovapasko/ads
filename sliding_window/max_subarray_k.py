# Find the max sum subarray of fixed size k

def max_sub_k(nums: list, k: int):
    sums = []
    m_sum = 0
    for i in range(len(nums) - k + 1):
        if i == 0:
            for j in range(k):
                m_sum += nums[j]
        else:
            m_sum -= nums[i-1]
            m_sum += nums[i + k - 1]
        sums.append(m_sum)
    return max(sums)


print(max_sub_k([1, 2, 4, 5, 3, 10], 3))
print(max_sub_k([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))
