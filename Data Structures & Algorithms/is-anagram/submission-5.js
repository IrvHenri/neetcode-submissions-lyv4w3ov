class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let sMap = {};
        let tMap = {};
        let result = false;

        if (s.length !== t.length) return false;
        for(let i = 0; i < s.length; i++){

            let currS = s[i];
            let currT = t[i];

            if(sMap[currS]){
               sMap[currS] += 1;   
            } else {
                sMap[currS] = 1;  
            }

            if(tMap[currT] ){             
               tMap[currT] += 1;
            } else {            
                tMap[currT] = 1;
            }

        }
    console.log(sMap,tMap)
        for( let key in sMap){
        
            if (tMap.hasOwnProperty(key) && tMap[key] === sMap[key]){
                result = true; 
            } else {
                return false;
            }
        }

        return result;
    }
}
