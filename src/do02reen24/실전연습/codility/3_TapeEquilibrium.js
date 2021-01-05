const solution = (A) => {
  let answer;
  let frontSum = 0;
  let backSum = A.reduce((a, b) => a + b, 0);
  for (let i = 0; i < A.length - 1; i += 1) {
    frontSum += A[i];
    backSum -= A[i];
    const absSub = Math.abs(frontSum - backSum);
    if (absSub < answer || answer === undefined) answer = absSub;
  }

  return answer;
};
