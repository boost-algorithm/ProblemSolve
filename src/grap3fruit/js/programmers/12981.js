const check = (words, n, word, idx, visited) => {
  if (visited.includes(word)) {
    return [(idx % n) + 1, Math.ceil((idx + 1) / n)];
  }
  if (idx > 0) {
    if (words[idx - 1][words[idx - 1].length - 1] !== word[0]) {
      return [(idx % n) + 1, Math.ceil((idx + 1) / n)];
    }
  }
  return null;
};

function solution(n, words) {
  let answer = null;
  const visited = [];

  words.forEach((word, idx) => {
    if (!answer) {
      answer = check(words, n, word, idx, visited);
      visited.push(word);
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

solution(n, words);
