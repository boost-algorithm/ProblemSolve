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
  let changedFlag = false;

  board.forEach((el) => {
    if (el[move - 1] !== 0 && changedFlag === false) {
      if (result.length > 0) {
        const prev = result.pop();

        if (prev === el[move - 1]) {
          el[move - 1] = 0;
          answer += 2;
          changedFlag = true;
        } else {
          result.push(prev);
        }
      }
      if (changedFlag === false) {
        result.push(el[move - 1]);
        el[move - 1] = 0;
        changedFlag = true;
      }
    }
  });
});

console.log(board);
console.log(result);
console.log(answer);
