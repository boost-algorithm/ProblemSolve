const checkPD = (word, idx) => {
  let max = 0;
  const wordLength = word.length;
  /* 
    2가지가 될수 있다.
    (1) baab
    (2) aba
    둘다 돌고 max 구하자!  
  */

  // 얘는 (2) aba
  max = 1;
  for (let i = 1; i < wordLength / 2; i++) {
    if (word[idx - i] !== word[idx + i]) {
      break;
    }
    max = i * 2 + 1;
  }

  // 얘는 (1) baab
  if (idx < word.length - 1 && word[idx] === word[idx + 1]) {
    let maxCheck2 = 2;
    if (maxCheck2 > max) {
      max = maxCheck2;
    }

    for (let i = 1; i < wordLength / 2; i++) {
      if (word[idx - i] !== word[idx + i + 1]) {
        break;
      }

      maxCheck2 = i * 2 + 2;
      if (maxCheck2 > max) {
        max = maxCheck2;
      }
    }
  }
  return max;
};

const solution = (s) => {
  let sArr = s.split('');
  let answer = 0;

  for (let i = 0; i < sArr.length; i++) {
    let result = checkPD(sArr, i);
    if (result > answer) {
      answer = result;
    }
  }

  return answer;
};

// solution('ccabcbaa');
console.log(solution('baaba'));
