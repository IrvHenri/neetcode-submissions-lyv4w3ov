class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
       
       
        this.capacity = capacity;
        this.arr = new Array(this.capacity).fill(0);
        this.length = 0;
       
       
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.arr[i];
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.arr[i] = n;
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {

        // if arr is at capacity, resize and then add
        if(this.length === this.capacity){
            this.resize();
        } 
        
        this.arr[this.length] = n;
        this.length ++;
        
    }

    /**
     * @returns {number}
     */
    popback() {
        if(this.length > 0){
        this.length --;
        
        }
         return this.arr[this.length];       
    }

    /**
     * @returns {void}
     */
    resize() {
        //double capacity 
        this.capacity = this.capacity * 2;
        // then shift current arr to placeholder arr, then assign placeholder to arr
        let tempArr = new Array (this.capacity);
            
        for(let i = 0; i < this.arr.length; i++){
            tempArr[i] = this.arr[i];
            
        }
        
        this.arr = tempArr;
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.length;
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        
        return this.capacity;
    }
}
