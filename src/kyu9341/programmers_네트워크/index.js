const initArray = (size, val = null) => Array.from({ length: size }, () => val);
const initArrayInArray = size =>
  Array.from({ length: size }, () => new Array());

const solution = (n, computers) => {
  const network = initArrayInArray(n);
  const check = initArray(n, false);

  computers.forEach((row, rowIdx) => {
    row.forEach((computer, colIdx) => {
      if (rowIdx !== colIdx && computer) network[rowIdx].push(colIdx);
    });
  });

  const dfs = (node, network) => {
    check[node] = true;

    network[node].forEach((_, computer) => {
      const next = network[node][computer];
      if (!check[next]) dfs(next, network);
    });
  };

  const answer = network.reduce((acc, _, computer) => {
    if (!check[computer]) {
      dfs(computer, network);
      return acc + 1;
    }
    return acc;
  }, 0);

  return answer;
};

(() => {
  const inputs = [
    [
      [1, 1, 0],
      [1, 1, 0],
      [0, 0, 1],
    ],
    [
      [1, 1, 0],
      [1, 1, 1],
      [0, 1, 1],
    ],
  ];

  inputs.forEach(input => console.log(solution(input.length, input)));
})();
