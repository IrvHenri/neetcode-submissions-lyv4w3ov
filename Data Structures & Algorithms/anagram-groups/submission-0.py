class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupMap = {}


        for str in strs:
            
            alphabet_ledger =  [0] * 26

            for char in str:
                position = ord(char) - 97
                alphabet_ledger[position] += 1
    
            key = tuple(alphabet_ledger)

            if key in groupMap:
                groupMap[key].append(str)
            else:
                groupMap[key] = [str]
      
        return list(groupMap.values())  