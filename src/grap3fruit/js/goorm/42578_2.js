function solution(clothes) {
  let answer = 1;
  console.log(clothes);

  const map = new Map();

  clothes.forEach((cloth) => {
    if (!map.get(cloth[1])) {
      return map.set(cloth[1], [cloth[0]]);
    }

    map.get(cloth[1]).push(cloth[0]);
  });

  for (let key of map.keys()) {
    answer *= map.get(key).length + 1;
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
