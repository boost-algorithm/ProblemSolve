const print = (N, info, data) => {
  console.log(N);
  console.log(info);
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
  console.log(line);
  if (!N) {
    N = +line;
  } else if (N && !info) {
    info = line.split(' ').map((el) => +el);
  } else {
    data.push(line.split(' ').map((el) => +el));
    // data.push(line.split('').map((el) => +el));
    // data.push(line.split('').map((el) => el));
    // data.push(line);
    count += 1;
  }
  if (count === N) {
    rl.close();
  }
}).on('close', function () {
  print(N, info, data);
  process.exit();
});
