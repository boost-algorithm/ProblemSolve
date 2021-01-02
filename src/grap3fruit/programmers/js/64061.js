const board = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 3],
  [0, 2, 5, 0, 1],
  [4, 2, 4, 4, 2],
  [3, 5, 1, 3, 1],
];
const moves = [1, 5, 3, 5, 1, 2, 1, 4];

function solution(board, moves) {
  const result = [];
  let answer = 0;

  moves.reduce((acc, move) => {
    for (let i = 0; i < board.length; i++) {
      if (board[i][move - 1] === 0) {
        continue;
      }

      if (acc.length > 0) {
        const prev = acc.pop();

        if (prev === board[i][move - 1]) {
          board[i][move - 1] = 0;
          answer += 2;
          return acc;
        }

        acc.push(prev);
      }

      acc.push(board[i][move - 1]);
      board[i][move - 1] = 0;
      return acc;
    }
    return acc;
  }, []);

  console.log(board);
  console.log(result);
  return answer;
}

console.log(solution(board, moves));
