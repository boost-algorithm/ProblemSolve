const getDividedArr = (arrA, arrB) => {
  return arrB.filter((el) => !arrA.includes(el));
};

function solution(s) {
  let answer = [];

  const arrS = s.split('');

  let mother_arr = [];
  let child_arr = [];

  for (let i = 1; i < arrS.length - 1; i++) {
    if (arrS[i] === '}') {
      mother_arr.push(child_arr);
      child_arr = [];
    }

    if (+arrS[i] >= 0) {
      if (+arrS[i - 1] >= 0) {
        const num = child_arr.pop();
        child_arr.push(Number(num + arrS[i]));
      } else {
        child_arr.push(+arrS[i]);
      }
    }
  }
  console.log(mother_arr); // 여기 까지 {} 문자열을 [] 배열로 바꿈.

  for (let i = 0; i < mother_arr.length; i++) {
    for (let j = 0; j < mother_arr.length; j++) {
      if (mother_arr[j].length === i + 1) {
        const [temp] = getDividedArr(answer, mother_arr[j]);
        answer.push(temp);
      }
    }
  }

  return answer;
}

console.log(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'));
console.log(solution('{{1,2,3},{2,1},{1,2,4,3},{2}}'));
console.log(solution('{{20,111},{111}}'));
console.log(solution('{{123}}'));
console.log(solution('{{4,2,3},{3},{2,3,4,1},{2,3}}'));
