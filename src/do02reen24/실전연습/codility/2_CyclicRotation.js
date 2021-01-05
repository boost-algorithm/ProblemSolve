const solution = (A, K) => {
  const length = A.length;
  const k = K % length;
  const front = A.slice(length - k, length);
  const end = A.slice(0, length - k);
  return front.concat(end);
};

console.log(solution([3, 8, 9, 7, 6], 3));
