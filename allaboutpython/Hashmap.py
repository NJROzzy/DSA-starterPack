from collections import defaultdict
class solution: 
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {defaultdict(list)}
        result = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        
        for value in anagram_map.values():
            result.append(value)
        
        return result
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = solution()
print(f"Grouped Anagrams: {solution.groupAnagrams(strs)}")