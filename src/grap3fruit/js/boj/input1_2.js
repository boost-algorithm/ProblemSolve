const solution = (N, info, data) => {
  console.log(N);
  const [X, Y] = info;
  console.log(X, Y);
  console.log(data);
};

let fs = require('fs');
let input = fs.readFileSync('test2').toString().split('\n');

const N = +input[0];
const info = input[1].split(' ').map((el) => +el);
const data = [];
for (let i = 2; i < N + 2; i++) {
  // 위에서 N을 받을떄 input[0]이 빠져나갔기 때문에 1~N을 받아야한다.
  data.push(input[i].split(' ').map((el) => +el));
}

solution(N, info, data);
