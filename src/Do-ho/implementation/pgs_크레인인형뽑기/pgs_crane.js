class CraneStack {
    constructor() {
        this.store = [];
        this.size = 0;
    }
    top() {
        if(this.size==0) return 0;
        return this.store[this.size-1];
    }
    pushAndGetResult(item) {
        if(this.top() === item) {
            this.pop();
            this.size--;
            return 2;
        }
        
        this.store.push(item);
        this.size++;
        return 0;
    }
    pop() { return this.store.pop(); } 
}

const pickDoll = (board, x) => {
    for(let i=0; i<board.length; i++) {
        if (board[i][x] != 0) {
            const result = board[i][x];
            board[i][x] = 0;
            return result;
        }
    }
    return 0;
}

const solution = (board, moves) => {
    let answer = 0;
    let basket = new CraneStack();
    
    moves.forEach((item) => {
        const doll = pickDoll(board, item-1);
        if(doll!==0) answer += basket.pushAndGetResult(doll);
    })
    
    return answer;
}