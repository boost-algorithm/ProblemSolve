const bfs = (computers, root) => {
  const visited = [root];
  let q = [computers[root]];

  while (q.length > 0) {
    let item = q.shift();

    item.forEach((el, idx) => {
      if (el === 1 && !visited.includes(idx)) {
        q.push(computers[idx]);
        visited.push(idx);
      }
    });
  }

  return visited;
};

function solution(n, computers) {
  let answer = 0;
  const visited = [];

  computers.forEach((_, idx) => {
    const visitFlag = visited.some((el) => el.includes(idx));

    if (!visitFlag) {
      const newVisited = bfs(computers, idx);
      visited.push(newVisited);
    }
  });

  console.log(visited.length);
  answer = visited.length;
  return answer;
}

const n = 3;
const computers = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
];
// const computers = [
//   [1, 1, 0],
//   [1, 1, 1],
//   [0, 1, 1],
// ];

solution(n, computers);
