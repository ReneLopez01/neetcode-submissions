class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        n = {}

        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            
            if word in n:
                n[word].append(strs[i])
            else:
                n[word] = [strs[i]]
        
        return list(n.values())