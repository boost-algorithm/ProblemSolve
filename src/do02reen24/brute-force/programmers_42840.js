function getScore(answers, userAnswers) {
  const userLength = userAnswers.length;
  return answers.reduce((sum, value, index) => {
    if (value === userAnswers[index % userLength]) return sum + 1;
    return sum;
  }, 0);
}

function solution(answers) {
  const answer = [];
  const ans1 = [1, 2, 3, 4, 5];
  const ans2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  const score1 = getScore(answers, ans1);
  const score2 = getScore(answers, ans2);
  const score3 = getScore(answers, ans3);

  const maxScore = Math.max(score1, score2, score3);

  if (maxScore === score1) answer.push(1);
  if (maxScore === score2) answer.push(2);
  if (maxScore === score3) answer.push(3);
  return answer;
}
