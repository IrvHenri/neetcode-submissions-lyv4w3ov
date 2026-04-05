class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
       let formatS = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
        let l = 0;
        let r = formatS.length - 1;

        while(l < r){
            if(formatS[l] !== formatS[r]){
                return false
            }

            l +=1;
            r -=1;
        }
       
       return true;
    }
}
