const solution = (N, info, data) => {
  console.log(N);
  const [X, Y] = info;
  console.log(X, Y);
  console.log(data);
};

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = null;
let info = null;
let count = 0;
const data = [];

rl.on('line', function (line) {
  if (!N) {
    // N이 null이면
    N = +line;
  } else if (!info) {
    // N이 null이 아닌데, info가 null이면
    info = line.split(' ').map((el) => +el);
  } else {
    // N과 info가 null이 아니면
    data.push(line);
    // data.push(line.split('').map((el) => +el));
    // data.push(line.split('').map((el) => el));
    // data.push(line.split(' ').map((el) => +el));
    count += 1; // data를 입력받으면 count를 증가시켜주고
  }
  if (count === N) {
    // count가 입력받아야하는 N일때 rl.close()를 호출해준다.
    rl.close();
  }
}).on('close', function () {
  // rl.close()를 호출하면 이 콜백함수로 들어오고
  solution(N, info, data); // solution을 실행 한 후
  process.exit(); // 프로세스를 종료한다.
});
