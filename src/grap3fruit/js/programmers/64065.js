const getSubtractedArr = (arrA, arrB) => arrB.filter((el) => !arrA.includes(el));

const getArrFromStr = (s) => {
  const arr = s.split('');

  let parent_arr = [];
  let child_arr = [];

  for (let i = 1; i < arr.length - 1; i++) {
    if (arr[i] === '}') {
      parent_arr.push(child_arr);
      child_arr = [];
    }

    if (+arr[i] >= 0) {
      if (+arr[i - 1] >= 0) {
        const num = child_arr.pop();
        child_arr.push(Number(num + arr[i]));
      } else {
        child_arr.push(+arr[i]);
      }
    }
  }
  return parent_arr;
};

function solution(s) {
  let answer = [];
  const arr = getArrFromStr(s);

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j].length === i + 1) {
        const [temp] = getSubtractedArr(answer, arr[j]);
        answer.push(temp);
        break;
      }
    }
  }

  return answer;
}

// console.log(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'));
// console.log(solution('{{1,2,3},{2,1},{1,2,4,3},{2}}'));
// console.log(solution('{{20,111},{111}}'));
// console.log(solution('{{123}}'));
// console.log(solution('{{4,2,3},{3},{2,3,4,1},{2,3}}'));

const setA = new Set();
const setB = new Set();
setA.add(1);
setA.add(2);
setB.add(3);
setB.add(2);

console.log(setA, setB);
console.log(setA - setB);
