const range = (start, end) =>
  start < end ? Array.from({ length: end - start + 1 }, (_, idx) => idx + start) : [];

const solution = (board, moves) => {
  let count = 0;
  const stack = [];

  const pickDoll = col => {
    for (const row of range(0, board.length - 1)) {
      const currentDoll = board[row][col - 1];
      board[row][col - 1] = 0;

      const isExist = currentDoll !== 0;
      const isEqualToPrevDoll = stack[stack.length - 1] === currentDoll;

      if (isExist) {
        if (isEqualToPrevDoll) {
          stack.pop();
          count += 2;
          break;
        }
        stack.push(currentDoll); 
        break;
      }
    }
  };
  
  moves.forEach(pickDoll);
  return count;
}

(() => {
  const board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]];
  const moves = [1,5,3,5,1,2,1,4];

  console.log(solution(board, moves));
})();

