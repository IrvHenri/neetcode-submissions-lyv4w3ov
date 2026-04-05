class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupMap = defaultdict(list)


        for str in strs:
            
            count =  [0] * 26

            for char in str:
                
                count[ord(char) - ord('a')] += 1
    
            key = tuple(count)

            groupMap[key].append(str)
      
        return list(groupMap.values()) 