# :fire: week14

- 이번주는 마이리얼트립 코딩테스트 준비를 위해 프로그래머스에서 `javascript`로 문제를 풀기로 하였다.

## :ballot_box_with_check: 프로그래머스 튜플(64065)

- python으로 문제를 풀다가 javascript로 문제를 푸니 헷갈렸다.
- 변수명과 함수 분리를 신경써서 코드를 작성하였다.

## :ballot_box_with_check: 프로그래머스 크레인 인형뽑기 게임(64061)

## :ballot_box_with_check: 프로그래머스 가장 긴 팰린드롬(12904)

#### 정확성: 62.7, 효율성: 30.7

- 테스트 6번 12번 실패

```js
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
  let length = oddPalindrome(word, start);
  if (length === 1) {
    const result = evenPalindrome(word, start);
    if (result > length) {
      length = result;
    }
  }
  return length;
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
```
