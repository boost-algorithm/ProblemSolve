const getMaxOddPalindrome = (word, idx) => {
  let max = 0;
  for (let i = 0; i < word.length / 2; i++) {
    if (word[idx - i] !== word[idx + i]) {
      break;
    }
    max = i * 2 + 1;
  }
  return max;
};

const getMaxEvenPalindrome = (word, idx) => {
  let max = 0;
  if (idx < word.length - 1 && word[idx] === word[idx + 1]) {
    for (let i = 0; i < word.length / 2; i++) {
      if (word[idx - i] !== word[idx + i + 1]) {
        break;
      }
      max = i * 2 + 2;
    }
  }
  return max;
};

const solution = (s) => {
  let sArr = s.split('');
  let answer = 0;

  for (let i = 0; i < sArr.length; i++) {
    answer = Math.max(answer, getMaxOddPalindrome(sArr, i), getMaxEvenPalindrome(sArr, i));
  }

  return answer;
};

// solution('ccabcbaa');
console.log(solution('baaba'));
