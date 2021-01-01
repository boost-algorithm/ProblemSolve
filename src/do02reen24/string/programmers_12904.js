const isSameWord = (word, pre, next) => {
  if (pre < 0 || next >= word.length) {
    return false;
  }
  if (word[pre] !== word[next]) {
    return false;
  }
  return true;
};

const oddPalindrome = (word, start) => {
  let index = 1;
  while (true) {
    const pre = start - index;
    const next = start + index;
    if (isSameWord(word, pre, next)) {
      index = index + 1;
      continue;
    }
    index = index - 1;
    break;
  }
  return index * 2 + 1;
};

const evenPalindrome = (word, start) => {
  let index = 0;
  while (true) {
    const pre = start - index;
    const next = start + 1 + index;
    if (isSameWord(word, pre, next)) {
      index = index + 1;
      continue;
    }
    break;
  }
  return index * 2;
};

const isPalindrome = (word, start) => {
  const oddResult = oddPalindrome(word, start);
  const evenResult = evenPalindrome(word, start);
  return Math.max(oddResult, evenResult);
};

const solution = (s) => {
  let maxLength = 0;
  for (let index = 0; index < s.length; index++) {
    const result = isPalindrome(s, index);
    if (maxLength < result) {
      maxLength = result;
    }
  }

  return maxLength;
};
