# made by Tonny Hoare
# doesn't require extra memory
import random

class QuickSelect:
    
    def __init__(self, nums):
        self.nums = nums
        self.first_index = 0
        self.last_index = len(nums) - 1
        
    def run(self,k):
        return self.select(self.first_index, self.last_index, k-1)
    
    # Partition Phase
    def partition(self, first_index, last_index):
        # generate random value with this range
        pivot_index = random.randint(first_index, last_index)
        
        self.swap(pivot_index, last_index)
        
        for i in range(first_index, last_index):
            # for smallest
            # if self.nums[i] < self.nums[last_index]:
            #     self.swap(i, first_index)
            #     first_index += 1
            # for largest
            if self.nums[i] > self.nums[last_index]:
                self.swap(i, first_index)
                first_index += 1
        
        self.swap(first_index, last_index)
        
        # index of the pivot
        return first_index
    
    def swap(self,i,j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
    
    # selection phase
    def select(self, first_index, last_index, k):
        pivot_index = self.partition(first_index, last_index)
        
        # selection phase when we compare the pivot_index with k
        
        if pivot_index < k:
            # discard left array
            # consider items on the right
            return self.select(pivot_index + 1, last_index, k)
        elif pivot_index > k:
            # we have to discard sub array
            return self.select(first_index, pivot_index -1, k)
        
        # found item
        return self.nums[pivot_index]
    

x = [1,2,-5,10,100,-7,3,4]
select = QuickSelect(x)
print(select.run(5))