const solution = (N, data) => {
  console.log(N);
  console.log(data);
};

let fs = require('fs');
let input = fs.readFileSync('test').toString().split('\n');

const N = +input[0];
const data = [];
for (let i = 1; i < N + 1; i++) {
  // 위에서 N을 받을떄 input[0]이 빠져나갔기 때문에 1~N을 받아야한다.
  data.push(input[i].split(' ').map((el) => +el));
}

solution(N, data);
