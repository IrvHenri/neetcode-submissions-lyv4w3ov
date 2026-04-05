class LinkedList {
    constructor() {
        
       
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {

        let curr = this.head.next;
        let i = 0;

        while(curr){

        if(i === index){
        
        return curr.val;
        
        }
        
        i++
        curr = curr.next;
     
        }

        return -1;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        const newNode = new ListNode(val);
        newNode.next = this.head.next;
        this.head.next = newNode;
        if (!newNode.next) {
            // If list was empty before insertion
            this.tail = newNode;
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
       
        this.tail.next = new ListNode(val);
        this.tail = this.tail.next;
        
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {

        let curr = this.head;
        let i = 0

        // get the index of the node just before the one to be removed
        while(i < index && curr){

            i++
            curr = curr.next;
        }
        // then set the next pponter of this node to the next next node.
        if(curr && curr.next){
            if(curr.next === this.tail){
                this.tail = curr;
            }
            curr.next = curr.next.next;

            return true
        }

        return false
    }

    /**
     * @return {number[]}
     */
    getValues() {

        let curr = this.head.next;
        let vals = [];
        while(curr){

            vals.push(curr.val);
            curr = curr.next;
        }

        return vals;
    }
}

class ListNode {
    constructor(val, nextNode = null){
        this.val = val;
        this.next = nextNode;
    }
}
