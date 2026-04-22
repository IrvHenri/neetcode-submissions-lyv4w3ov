class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1,n2 = len(s1),len(s2)

        if n1 > n2:
            return False

        cnt1 = [0] * 26

        for ch in s1:
            cnt1[ord(ch) - ord('a')] +=1
        
        cnt2 = [0] * 26

        for i in range(n1):
            cnt2[ord(s2[i]) - ord('a')] +=1
        
        def same_counts(a,b):
            for i in range(26):
                if a[i] != b[i]:
                    return False
            return True
        
        if same_counts(cnt1,cnt2):
            return True
        # start fron n1, and begin to slide window

        
        for r in range(n1,n2):

            cnt2[ord(s2[r]) - ord('a')] +=1
            l = r - n1
            cnt2[ord(s2[l]) - ord('a')] -=1

            if same_counts(cnt1,cnt2):
                return True
        return False


        