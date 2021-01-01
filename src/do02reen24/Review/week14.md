# :fire: week14

- 이번주는 마이리얼트립 코딩테스트 준비를 위해 프로그래머스에서 `javascript`로 문제를 풀기로 하였다.

## :ballot_box_with_check: 프로그래머스 튜플(64065)

- python으로 문제를 풀다가 javascript로 문제를 푸니 헷갈렸다.
- 변수명과 함수 분리를 신경써서 코드를 작성하였다.

## :ballot_box_with_check: 프로그래머스 크레인 인형뽑기 게임(64061)

#### 정확성 81.8

- 테스트 1번, 2번 실패

```js
const getTopDollIndex = (board, index) => {
  let topIndex = -1;
  for (const line of board) {
    topIndex = topIndex + 1;
    if (line[index] !== 0) break;
  }
  return topIndex;
};

const solution = (board, moves) => {
  let answer = 0;
  const basket = [];
  for (const move of moves) {
    const dollX = move - 1;
    const dollY = getTopDollIndex(board, dollX);
    const doll = board[dollY][dollX];
    board[dollY][dollX] = 0;

    const top = basket.pop();
    if (top === doll) {
      answer = answer + 2;
    } else {
      basket.push(top);
      basket.push(doll);
    }
  }
  return answer;
};
```

- 해당 열에 남은 인형이 없을 경우 예외처리를 해주었어야 했는데 기존의 코드는 0을 넣어주는 문제가 있음을 알게 되었다. 이에 대한 예외처리를 진행하여 해결할 수 있었다.

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

- 처음 코드에서는 홀수 검사 결과가 있다면 짝수 검사를 진행하지 않았었는데, 짝수 검사의 결과가 더 큰 경우도 존재함을 알게 되었다. 따라서 두 경우를 모두 계산해주고 더 큰 값을 반환해주도록 변경하였다.
