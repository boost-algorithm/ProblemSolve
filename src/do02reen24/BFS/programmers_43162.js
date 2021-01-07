const solution = (n, computers) => {
  let answer = 0;
  const network = Array.from({ length: n }, () => 0);

  for (let i = 0; i < n; i += 1) {
    if (network[i] !== 0) continue;
    answer += 1;
    network[i] = answer;

    const queue = [i];
    while (queue.length > 0) {
      const visit = queue.pop();
      computers[visit].forEach((computer, index) => {
        if (computer && network[index] === 0) {
          queue.push(index);
          network[index] = answer;
        }
      });
    }
  }

  return answer;
};
