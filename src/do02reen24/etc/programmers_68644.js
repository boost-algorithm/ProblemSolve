function sortAsc(a, b) {
  return a - b;
}

function getKeys(dict) {
  const keys = [];
  for (const key in dict) keys.push(Number(key));
  return keys.sort(sortAsc);
}

function solution(numbers) {
  const dict = {};
  for (let a = 0; a < numbers.length; a++) {
    for (let b = a + 1; b < numbers.length; b++) {
      const sum = numbers[a] + numbers[b];
      dict[sum] = true;
    }
  }

  return getKeys(dict);
}
