class LinkedList {
    constructor() {
        this.head = new listNode(-1);
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
            i++;
            curr = curr.next;
        }

        return -1;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        let newHead = new listNode(val);
        newHead.next = this.head.next;
        this.head.next = newHead;

        if (!newHead.next) {
            // If list was empty before insertion
            this.tail = newHead;
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let newTail = new listNode(val);
        this.tail.next = newTail;
        this.tail = this.tail.next;
 
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        let i = 0;
        let curr = this.head;
        // go through each node up until index before target index,
        while(curr && i < index){
 
            i++
            curr = curr.next;
        }


        if(curr && curr.next){
            if(curr.next === this.tail){
                this.tail = curr;
                
            }

            curr.next = curr.next.next;
            return true;
        }
            // if currents next.next is null then you are deleting the tail. update curr.next to null and curr = tail
                // if not then you set curr.next = curr.next.next;
        return false;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let vals = [];
        let curr = this.head.next;

        while(curr){
            vals.push(curr.val);
            curr = curr.next;
        }

        return vals
    }
}

class listNode {
    constructor( val, nextNode = null){
        this.val = val;
        this.next = nextNode;
    }
}
