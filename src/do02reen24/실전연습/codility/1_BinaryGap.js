const solution = (N) => {
  let maxLength = 0;
  const bin = N.toString(2).split('');

  bin.reduce((length, word) => {
    if (word === '1') {
      if (maxLength < length) maxLength = length;
      return 0;
    }
    return length + 1;
  }, 0);

  return maxLength;
};

console.log(solution(32));
