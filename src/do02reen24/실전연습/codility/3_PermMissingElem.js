const solution = (A) => {
  const N = A.length + 1;
  const isNum = {};
  A.forEach((a) => {
    isNum[a] = true;
  });
  for (let n = 1; n < N + 1; n += 1) {
    if (isNum[n] === true) continue;
    return n;
  }
  return -1;
};
