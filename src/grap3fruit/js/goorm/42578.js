function solution(clothes) {
  let answer = 1;
  const data = {};

  clothes.forEach((cloth) => {
    if (!data[cloth[1]]) {
      return (data[cloth[1]] = [cloth[0]]);
    }
    data[cloth[1]].push(cloth[0]);
  });

  for (const el in data) {
    answer *= data[el].length + 1;
  }
  answer -= 1;

  return answer;
}

const clothes = [
  ['yellow_hat', 'headgear'],
  ['blue_sunglasses', 'eyewear'],
  ['green_turban', 'headgear'],
];

console.log(solution(clothes));
