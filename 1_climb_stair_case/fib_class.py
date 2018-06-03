  
class Solution:
    
    def climb_stair(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climb_stair(n - 1) + self.climb_stair(n - 2)