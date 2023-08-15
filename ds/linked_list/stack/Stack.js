"use strict";
Object.defineProperty(exports, "__esModule", { value: true });

class Node {
    constructor(data) {
        this.data = data;
        this.prev = undefined;
    }
}

class Stack {
    constructor() {
        this.head = undefined;
    }

    push(item) {
        let node = new Node(item);

        if (this.head === undefined) {
            this.head = node;
            return;
        }

        node.prev = this.head;
        this.head = node;
    }

    pop() {
        if (this.head === undefined) {
            return undefined;
        }
        
        let head = this.head;
        this.head = this.head.prev;
        return head.data;
    }

    peek() {
        if (this.head === undefined) {
            return undefined;
        }

        return this.head.data;
    }
}
exports.default = Stack;

// TEST...
let stk = new Stack();
console.log(stk.peek());
// stk.push(42);
// stk.push(-42);
// console.log(stk.pop());
// console.log(stk.pop());
// console.log(stk.pop());
// console.log(stk.peek());
// ...TES}T