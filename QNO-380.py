import random
class RandomizedSet(object):

    def __init__(self):
        self.val_idx = {}  # maps value to its index in nums
        self.nums = [] # stores the actual values
        

    def insert(self, val):
        if val in self.val_idx:
            return False
        self.nums.append(val)
        self.val_idx[val] = len(self.nums)-1
        return True
        

    def remove(self, val):
        if val not in self.val_idx:
            return False
        self.nums.remove(val)
        del self.val_idx[val]
        return True

    def getRandom(self):
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()