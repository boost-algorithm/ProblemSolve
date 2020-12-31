const countingNumber = (arr) => {
  const counts = {};
  arr.forEach((n) => (counts[n] = (counts[n] || 0) + 1));
  return counts;
};

const sortByValue = (dict) => {
  const arr = [];
  for (const key in dict) {
    const value = dict[key];
    arr.push([Number(key), value]);
  }
  return arr.sort((pre, next) => next[1] - pre[1]);
};

const getKeyList = (arr) => {
  const keys = [];
  for (const pair of arr) {
    const key = pair[0];
    keys.push(key);
  }
  return keys;
};

const solution = (s) => {
  const deleteBracket = s.replace(/[{}]/gi, '');
  const numberList = deleteBracket.split(',');
  const counts = countingNumber(numberList);
  const valueList = sortByValue(counts);
  const answer = getKeyList(valueList);
  return answer;
};
