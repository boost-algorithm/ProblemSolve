const solution = (N, data) => {
  console.log(N);
  console.log(data);
};

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let T = null;
let N = null;
let info = null;
let countN = 0;
let countT = 0;
let data = [];

rl.on('line', function (line) {
  if (!T) {
    T = +line;
  } else if (!N) {
    N = +line;
  } else {
    data.push(line);
    // data.push(line.split('').map((el) => +el));
    // data.push(line.split('').map((el) => el));
    // data.push(line.split(' ').map((el) => +el));
    countN += 1; // data를 입력받으면 countN을 증가시켜주고
  }
  if (countN === N) {
    // N만큼 data를 잘 입력 받았으면
    solution(N, data); // solution을 호출하고
    N = null; // T, countT를 제외한 값들을 초기화해준다.
    info = null;
    countN = 0;
    data = [];

    countT += 1; // 그리고 테스트 케이스 하나를 통과했으니 countT를 1 올려준다.
  }
  if (countT === T) {
    // 입력받은 T 만큼 테스트 케이스를 통과하게되면
    rl.close(); // rl.close()를 호출하고
  }
}).on('close', function () {
  process.exit(); // 종료한다.
});
