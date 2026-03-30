class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_array = []
        hash_map = {}
        count = 0
        for i in strs:
            initial_arr = [0] * 25
            for j in i:
                res = ord(j) % len(initial_arr)
                initial_arr[res] = initial_arr[res] + 1
            
            if tuple(initial_arr) in hash_map:
                final_array[hash_map[tuple(initial_arr)]].append(i)
            else:
                hash_map[tuple(initial_arr)] = count
                final_array.append([i])
                count += 1
    
        return final_array
                