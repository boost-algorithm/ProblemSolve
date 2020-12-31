const parseStringToArray = str => str.substring(2, str.length - 2)
                                .split("},{")
                                .map(el => el.split(',').map(str => Number(str)));

const solution = s => {
  const set = new Set();
  const arr = parseStringToArray(s);
  
  const compareLength = (prev, cur) => prev.length - cur.length;
  arr.sort(compareLength).flat().forEach(el => set.add(el));;

  return [...set];
}

(() => {
  const inputs = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}",
  ];

  inputs.forEach(input => console.log(solution(input)));
})();

