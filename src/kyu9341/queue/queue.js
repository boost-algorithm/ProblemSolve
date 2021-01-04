class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(data) {
    const node = new Node(data);
    if (this.isEmpty()) {
      this.head = node;
      this.head.next = this.tail;
    } else this.tail.next = node;

    this.tail = node;
    this.size += 1;
  }

  pop() {
    if (this.isEmpty()) return null;
    if (this.head === this.tail) this.tail = null;

    const headData = this.head.data;
    this.head = this.head.next;
    this.size -= 1;

    return headData;
  }

  isEmpty() {
    return this.size === 0;
  }

  getArray() {
    const array = [];
    if (this.isEmpty()) return array;

    let currentNode = this.head;
    while (currentNode) {
      array.push(currentNode.data);
      currentNode = currentNode.next;
    }

    return array;
  }
}
