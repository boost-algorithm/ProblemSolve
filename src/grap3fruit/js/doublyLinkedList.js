class Node {
  constructor(item) {
    this.prev = null;
    this.next = null;
    this.item = item;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = new Node(null);
    this.tail = new Node(null);
    this.head.next = this.tail;
    this.tail.prev = this.head;
    this.length = 0;
  }

  getLength() {
    return this.length;
  }

  push(item) {
    const node = new Node(item);
    this.length += 1;

    if (this.head.next === this.tail) {
      node.prev = this.head;
      node.next = this.tail;
      this.head.next = node;
      this.tail.prev = node;
      return;
    }

    let lastNode = this.tail.prev;
    node.next = this.tail;
    node.prev = lastNode;
    lastNode.next = node;
    this.tail.prev = node;
    return;
  }

  print() {
    let current = this.head.next;
    while (true) {
      if (current === this.tail) {
        return;
      }
      console.log(current.item);
      current = current.next;
    }
  }

  pop() {
    if (this.length === 0) {
      return undefined;
    }
    this.length -= 1;
    const popedNode = this.tail.prev;
    popedNode.prev.next = this.tail;
    this.tail.prev = popedNode.prev;
    return popedNode.item;
  }

  popLeft() {
    if (this.length === 0) {
      return undefined;
    }
    this.length -= 1;
    const popedNode = this.head.next;
    popedNode.next.prev = this.head;
    this.head.next = popedNode.next;
    return popedNode.item;
  }

  filter(callback) {
    let current = this.head.next;
    const result = [];
    while (current !== this.tail) {
      console.log(current.item);
      if (callback(current.item)) {
        result.push(current.item);
      }
      current = current.next;
    }
    return result;
  }
}

const dl = new DoublyLinkedList();

dl.push([1, 0]);
dl.push([2, 1]);
dl.push([3, 1]);
dl.push([4, 2]);
dl.push([5, 2]);
console.log(dl.filter((el) => el[0] === 1 && el[1] === 0));
console.log('---');
console.log(dl.getLength());
console.log('---');
console.log(dl.popLeft());
console.log('---');
dl.print();
console.log('---');
console.log(dl.pop());
console.log('---');
console.log(dl.getLength());
console.log('---');
dl.print();
