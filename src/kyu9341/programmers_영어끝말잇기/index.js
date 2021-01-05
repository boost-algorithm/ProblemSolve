const solution = (n, words) => {
  const set = new Set();
  let prevWrod = '';

  for (const [idx, word] of words.entries()) {
    const beNotEqual =
      idx && prevWrod.charAt(prevWrod.length - 1) !== word.charAt(0);

    if (set.has(word) || beNotEqual) {
      const num = (idx + 1) % n || n;
      const count = Math.floor((idx + 1) / n) + Number(num !== n);

      return [num, count];
    }

    set.add(word);
    prevWrod = word;
  }

  return [0, 0];
};

(() => {
  const inputs = [
    {
      n: 3,
      words: [
        'tank',
        'kick',
        'know',
        'wheel',
        'land',
        'dream',
        'mother',
        'robot',
        'tank',
      ],
    },
    {
      n: 5,
      words: [
        'hello',
        'observe',
        'effect',
        'take',
        'either',
        'recognize',
        'encourage',
        'ensure',
        'establish',
        'hang',
        'gather',
        'refer',
        'reference',
        'estimate',
        'executive',
      ],
    },
    { n: 2, words: ['hello', 'one', 'even', 'never', 'now', 'world', 'draw'] },
  ];

  inputs.forEach(input => console.log(solution(input.n, input.words)));
})();
