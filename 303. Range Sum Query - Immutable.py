class NumArray:

    
    def __init__(self, nums: list[int]):
        self.nums_sum = []
        sum = 0
        for i in nums:
            sum = sum + i
            self.nums_sum.append(sum)
        print(self.nums_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums_sum[right]
        else:
            return self.nums_sum[right] - self.nums_sum[left-1]


# Your NumArray object will be instantiated and called as such:

obj = NumArray([-2,0,3,-5,2,-1])
# param_1 = obj.sumRange(left,right)