function solution(progresses, speeds) {
  let answer = [];
  const finishDay = progresses.map((progress, index) =>
    Math.ceil((100 - progress) / speeds[index])
  );
  let max;
  let count = 0;

  finishDay.forEach((element) => {
    if (!max) max = element;
    else if (max < element) {
      answer.push(count);
      count = 0;
      max = element;
    }
    count++;
  });
  answer.push(count);
  return answer;
}
