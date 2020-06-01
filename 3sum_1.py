from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.unique_pairs_dict = defaultdict(list)

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.unique_pairs_dict.clear()
        if len(nums) <= 2:
            return []
        n = len(nums)
        result_list = {}
        for i in range(n):
            for j in range(i+1, n):
                cur_pair = [nums[i], nums[j]]
                pair_sum = cur_pair[0] + cur_pair[1]
                if self.is_pair_seen(cur_pair):
                    j += 1
                    continue
                else:
                    self.unique_pairs_dict[pair_sum].append(cur_pair)
                
                rem_arr = nums[0:i] + nums[i+1: j] + nums[j+1:]
                if self.is_element_with_value(0 - pair_sum, rem_arr):
                    res = cur_pair[:] + [0 - pair_sum]
                    res.sort()
                    key = ','.join(str(elem) for elem in res)
                    result_list[key] = res
                j += 1
            i += 1
        
        return result_list.values().sort()
        
        
    def is_equal_pair(self, pair1, pair2):
        if pair1[0] == pair2[0] and pair1[1] == pair2[1] or \
           pair1[0] == pair2[1] and pair1[1] == pair2[0]:
            return True
        return False
    
    def is_pair_seen(self, pair):
        pair_sum = pair[0] + pair[1]
        if pair_sum in self.unique_pairs_dict:
            pair_list = self.unique_pairs_dict[pair_sum]
            if any(1 for p in pair_list if self.is_equal_pair(p, pair)):
                return True
        return False

    def is_element_with_value(self, target_val, arr):
        return any(1 for elem in arr if elem == target_val)
