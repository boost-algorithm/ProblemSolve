// Run by Node.js
const getResultLength = (data) => {
  dataArr = data[0].split('');
  // console.log(dataArr)
  const result = dataArr.filter((el) => el === data[1]);
  return result.length;
};

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let count = 0;
let n = 2;
data = [];
rl.on('line', function (line) {
  data.push(line);
  count += 1;
  if (count === n) {
    rl.close();
  }
}).on('close', function () {
  console.log(getResultLength(data));
  process.exit();
});
