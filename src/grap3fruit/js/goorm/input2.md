test case

```
5
12345
23456
34567
45678
56789
```

결과

```
5
[
  [1,2,3,4,5],
  [2,3,4,5,6],
  [3,4,5,6,7],
  [4,5,6,7,8],
  [5,6,7,8,9]
]
```

```javascript
const print = (N, data) => {
  console.log(N);
  console.log(data);
};

const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let N = null;
  let count = 0;
  const data = [];

  for await (const line of rl) {
    if (!N) {
      N = +line;
    } else {
      // data.push(line); // 1 2 3 4 5 -> ['1 2 3 4 5']
      // data.push(line.split(' ').map((el) => +el)); // 1 2 3 4 5 -> [1,2,3,4,5]
      // data.push(line.split('').map((el) => el));   // 12345 -> ['1','2','3','4','5']
      data.push(line.split('').map((el) => +el)); // 12345 -> [1,2,3,4,5]
      count += 1;
    }
    if (N === count) {
      rl.close();
    }
  }

  data.forEach((el) => {
    console.log('len: ', el.length);
  });

  print(N, data);
  process.exit();
})();
```
