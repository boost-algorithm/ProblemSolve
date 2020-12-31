const getTopDollIndex = (board, index) => {
  let topIndex = -1;
  for (const line of board) {
    topIndex = topIndex + 1;
    if (line[index] !== 0) {
      return topIndex;
    }
  }
  return -1;
};

const solution = (board, moves) => {
  let answer = 0;
  const basket = [];

  for (const move of moves) {
    const dollX = move - 1;
    const dollY = getTopDollIndex(board, dollX);
    if (dollY === -1) continue;

    const doll = board[dollY][dollX];
    board[dollY][dollX] = 0;

    const top = basket.pop();
    if (top === doll) {
      answer = answer + 2;
      continue;
    } else if (top) {
      basket.push(top);
    }
    basket.push(doll);
  }

  return answer;
};
