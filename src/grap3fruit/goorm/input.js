const print = (N, data) => {
  console.log(N);
  console.log(data);
};

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = null;
let count = 0;
const data = [];

rl.on('line', function (line) {
  console.log(line);
  if (!N) {
    N = +line;
  } else {
    // data.push(line.split(' ').map((el) => +el));
    // data.push(line.split('').map((el) => +el));
    // data.push(line.split('').map((el) => el));
    data.push(line);
  }
  count += 1;
  if (count === N) {
    rl.close();
  }
}).on('close', function () {
  print(N, data);
  process.exit();
});
