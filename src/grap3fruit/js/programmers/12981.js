const getResult = (idx, n) => {
  return [(idx % n) + 1, Math.ceil((idx + 1) / n)];
};

const check = (lastWord, n, word, idx, visited) => {
  if (visited.get(word)) {
    return getResult(idx, n);
  }
  if (idx > 0) {
    if (lastWord[lastWord.length - 1] !== word[0]) {
      return getResult(idx, n);
    }
  }
  return null;
};

function solution(n, words) {
  let answer = null;
  const visited = new Map();

  words.forEach((word, idx) => {
    if (!answer) {
      answer = check(words[idx - 1], n, word, idx, visited);
      visited.set(word, true);
    }
  });
  if (!answer) {
    answer = [0, 0];
  }
  return answer;
}

const n = 2;
const words = ['hello', 'two'];
// const words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'];
// const words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'];

console.log(solution(n, words));
