const board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];
const moves = [1, 5, 3, 5, 1, 2, 1, 4];

const result = [];
let answer = 0;

moves.forEach((move) => {
  for (let i = 0; i < board.length; i++) {
    if (board[i][move - 1] !== 0) {
      if (result.length > 0) {
        const prev = result.pop();

        if (prev === board[i][move - 1]) {
          board[i][move - 1] = 0;
          answer += 2;
          break;
        }

        result.push(prev);
      }

      result.push(board[i][move - 1]);
      board[i][move - 1] = 0;
      break;
    }
  }
});

console.log(board);
console.log(result);
console.log(answer);
