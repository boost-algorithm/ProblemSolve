const print = (data) => {
  console.log(data);
};

const getTrashCount = (data, A, B, K) => {
  let count = 0;
  for (let i = A; i < A + K; i++) {
    for (let j = B; j < B + K; j++) {
      if (data[i][j] === 1) {
        count += 1;
      }
    }
  }
  return count;
};

const solution = (data, info) => {
  const [N, K] = info;
  let min_result = K * K;
  for (let i = 0; i < N - K + 1; i++) {
    for (let j = 0; j < N - K + 1; j++) {
      min_result = Math.min(min_result, getTrashCount(data, i, j, K));
    }
  }
  console.log(min_result);
};

const readline = require('readline');

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let T = null;
  let info = null; // N, K
  let data = [];
  let count_T = 0;
  let count_N = 0;
  for await (const line of rl) {
    if (!T) {
      T = +line;
    } else if (T && !info) {
      info = line.split(' ').map((el) => +el);
    } else {
      data.push(line.split(' ').map((el) => +el));
      count_N += 1;
    }
    if (T && info) {
      if (info[0] === count_N) {
        // 로직 수행 & 초기화
        print(data);
        solution(data, info);

        info = null; // N, K
        data = [];
        count_T = 0;
        count_N = 0;
      }
    }
  }

  // rl.close();

  process.exit();
})();
