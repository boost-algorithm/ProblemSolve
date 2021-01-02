// Run by Node.js

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N = 0;
// const data = [];
let count = 0;

rl.on('line', function (line) {
  if (!N) {
    N = +line;
  } else {
    const data = line.split(' ').map((el) => +el);
    let min = data[0];
    for (let i = 1; i < data.length; i++) {
      if (data[i] < min) {
        min = data[i];
      }
    }
    console.log(min);
    rl.close();
  }
}).on('close', function () {
  process.exit();
});
