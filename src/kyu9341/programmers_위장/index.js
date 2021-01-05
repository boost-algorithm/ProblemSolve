const solution = clothes => {
  const clothesMap = clothes.reduce((map, cur) => {
    const countOfCurrentType = map.get(cur[1]);

    return map.set(cur[1], countOfCurrentType ? countOfCurrentType + 1 : 1);
  }, new Map());

  const count =
    [...clothesMap.values()].reduce((acc, cur) => acc * (cur + 1), 1) - 1;
  return count;
};

(() => {
  const inputs = [
    [
      ['yellow_hat', 'headgear'],
      ['blue_sunglasses', 'eyewear'],
      ['green_turban', 'headgear'],
    ],
  ];

  inputs.forEach(input => console.log(solution(input)));
})();
