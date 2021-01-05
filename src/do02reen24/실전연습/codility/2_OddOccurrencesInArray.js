const solution = (A) => {
  const count = A.reduce((arr, num) => {
    if (arr[num] === undefined) arr[num] = 1;
    else arr[num] += 1;
    return arr;
  }, {});
  for (const num in count) {
    if (count[num] % 2 !== 0) return num;
  }
  return -1;
};
